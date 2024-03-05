import scrython
import random

player_triggers = ["Sacrifice a NOUN",
         "Search your library",
         "Discard one or more cards",
         "Lose life",
         "Gain life",
         "Draw your first card each turn",
         "Draw your second card each turn",
         "Add RANDMANA mana of any color",
         "Scry",
         "Surveil",
         "Exile a permanent",
         "Tap a permanent",
         "Attach a permanent",
         "Counter a spell",
         "Mill one or more cards",
         "Shuffle your library",
         "Copies a spell",
         "Create one or more tokens",
         "Cast a spell",]
permanent_triggers = ["Becomes tapped",
         "Dies",
         "Enters the battlefield",
         "Is sacrificed",
         "Is flipped",
         "Is exiled",
         "Untaps",
         "Becomes blocked",
         "Attacks",
         "Attacks the player with the most life",
         "Attacks the player with the least life",
         "Has a counter placed on it",
         "Fights",
         "Create",
         "Cast a spell that targets this permanent",]
effects = ["Destroy target NOUN",
           "Sacrifice a NOUN",
           "Search your library for a NOUN",
           "Amass Orcs RAND",
           "Discard RAND cards",
           "Lose RAND life",
           "Gain RAND life",
           "Draw RAND cards",
           "Goad RAND creatures",
           "Exile RAND NOUNs",
           "Reveal RAND cards fom your hand",
           "Add RANDMANA mana of any color",
           "Scry RAND",
           "Surveil RAND",
           "Exile target NOUN, then return it to the battlefield",
           "Tap target NOUN",
           "Attach target NOUN to a NOUN",
           "Counter target NOUN",
           "Mill RAND",
           "Mill cards until you mill a NOUN",
           "Shuffle your library",
           "Copy target NOUN",
           "Fight target NOUN",
           "Create a Treasure token",
           "Create a RAND/RAND RANDCT token",
           "Bolster RAND",
           "Detain target NOUN",
           "Target NOUN explores",
           "Populate",
           "Proliferate",
           "Support RAND",
           
           ]
nouns = ["Player",
         "Creature",
         "Artifact",
         "Enchantment",
         "Graveyard",
         "Library",
         "Land",
         "Basic land",
         "Permanent",
         "Token",
         "Aura",
         "Equipment",
         "Saga",
         "Counter",
         "Token",
         "Card",
         "RANDCT",
         "RANDCT",
         "RANDCT",
         "RANDCT",
         "RANDCT",]
universal_additions = ["Affinity for NOUN",
                       "NOUNcycling RANDMANA",
                       "Kicker RANDMANA",
                       "Flash",
                       "Cascade",
                       "Convoke",
                       "Cycling RANDMANA",
                       "Delve",
                       "Dredge RAND",
                       "Epic",
                       "Fortell RANDMANA",
                       "Storm",
                       "Gravestorm",
                       "Multikicker RANDMANA",
                       "Suspend RAND -- RANDMANA",
                       
    ]

permanent_additions = ["Hexproof",
                       "Indestructible",
                       "Ward RANDMANA",
                       "Exalted",
                       "Cumulative upkeep RANDMANA",
                       "Echo RANDMANA",
                       "Fabricate RAND",
                       "Fading RAND",
                       "Madness RANDMANA",
                       
    ]

instsorc_additions = ["Flashback RANDMANA",
                      "Overload RANDAMANA",
                      "Rebound",
                      ]
                      

creature_additions = [
             "Protection from NOUNs",
             "Haste",
             "Menace",
             "Flying",
             "Reach",
             "Vigilance",
             "Trample",
             "Prowess",
             "Deathtouch",
             "Annihilator RAND",
             "Crew RAND",
             "Defender",
             "Double strike",
             "First strike",
             "Lifelink",
             "Fear",
             "Bands with NOUN",
             "Bloodthirst RAND",
             "Bushido RAND",
             "Champion a NOUN",
             "Dash RANDMANA",
             "Devour RAND",
             "Evolve",
             "Evoke RANDMANA",
             "Horsemanship",
             "Infect",
             "Mentor",
             "RANDMANA: Monstrosity RAND",
             "Ninjutsu RANDMANA",
             "Persist",
             "Renown RAND",
             "Shadow",
             "Sunburst RAND",
             "Undying",
             "Wither",
             ]


class Card:
    name = "CardName"
    typeLine = "Type"
    manaCost = "4R"
    description = ""
    rarity = "C"
    pnt = "0/1"

    def __init__(self, _name, _typeLine, _manaCost, _description, _rarity, _pnt):
        self.name = _name
        self.typeLine = _typeLine
        self.manaCost = _manaCost
        self.description = _description
        self.rarity = _rarity
        self.pnt = _pnt

    def to_string(self):
        return self.name + "\n" + self.manaCost + " " + self.typeLine + "\nDescription: " + self.description + "\nRarity: " + self.rarity + "\nP/T: " + self.pnt;

def parse_string(_string):
    string = _string
    string = string.replace("NOUN", str(nouns[random.randint(0, len(nouns) - 1)]).lower())
    string = string.replace("RANDMANA", "{" + rand_mana_cost() + "}")
    card = scrython.cards.Random()
    if "RANDCT" in string:
        string = string.replace("RANDCT", get_creature_type())
    if "randct" in string:
        string = string.replace("randct", get_creature_type())
    string = string.replace("RAND", str(random.randint(1, 5)))
    return string

# print (parse_string(additions[1]))

def rand_player_trigger():
    return parse_string(player_triggers[random.randint(0, len(player_triggers) - 1)])

def rand_permanent_trigger():
    return parse_string(permanent_triggers[random.randint(0, len(permanent_triggers) - 1)])

def rand_effect():
    return parse_string(effects[random.randint(0, len(effects) - 1)])

def rand_noun():
    return parse_string(nouns[random.randint(0, len(nouns) - 1)])

def rand_add(cardType, numKWstr):
    numKeywords = (random.randint(0, 2))
    if numKWstr != "rand":
        numKeywords = int(numKWstr)
    match cardType:
        case "creature":
            kwList = universal_additions + permanent_additions + creature_additions;
            ret = ""
            counter = 0
            for i in range(numKeywords):
                counter+=1
                if (counter == 0):
                    ret += (parse_string(kwList[random.randint(0, len(kwList) - 1)]))
                    ret += ", "
                elif (counter != numKeywords):
                    ret += (parse_string(kwList[random.randint(0, len(kwList) - 1)])).lower()
                    ret += ", "
                else:
                    ret += (parse_string(kwList[random.randint(0, len(kwList) - 1)])).lower()
            return ret
        case "artifact" | "enchantment":
            kwList = universal_additions + permanent_additions;
            return parse_string(kwList[random.randint(0, len(kwList))])
        case "instant" | "sorcery":
            kwList = universal_additions + instsorc_additions;
            return parse_string(kwList[random.randint(0, len(kwList))])

    return ""

def rand_mana_cost():
    card = scrython.cards.Random()
    
    try:
        return card.mana_cost().lower()
    except:
        return "{0}"

def rand_rarity():
    rarities = ["Common", "Uncommon", "Rare", "Mythic Rare"]
    return rarities[random.randint(0, 3)]

def rand_ct():
    types = get_creature_type().split(" ")
    return types[0]

def rand_pnt(mana_cost):
    return str(str(get_mana_value(mana_cost) + random.randint(-abs(get_mana_value(mana_cost)), get_mana_value(mana_cost))) + "/" + str(get_mana_value(mana_cost) + random.randint(-get_mana_value(mana_cost), get_mana_value(mana_cost)) + 1))

def rand_name():
    card1 = scrython.cards.Random().name()
    card2 = scrython.cards.Random().name()
    card1names = card1.split(" ")
    card2names = card2.split(" ")
    return card1names[0] + " " + card2names[len(card2names) - 1]

def get_mana_value(mana_cost):
    res = []
    x=mana_cost.split()
    for i in x:
        if i.isnumeric():
            res.append(int(i))
    if len(res) == 0:
        return len(mana_cost.replace("{", "").replace("}", ""))
    print("Mana value: " + res[0] + len(mana_cost.replace("{", "").replace("}", "")) - 1)
    return res[0] + len(mana_cost) - 1

def get_creature_type():
    card = scrython.cards.Random()
    typ = str(card.type_line())
    while "Creature" not in typ:
        card = scrython.cards.Random()
        typ = str(card.type_line())
    typ = typ.replace("Artifact Creature — ", "")
    typ = typ.replace("Legendary Creature — ", "")
    typ = typ.replace("Snow Creature — ", "")
    typ = typ.replace("Creature — ", "")
    return typ

def get_creature_type_line():
    card = scrython.cards.Random()
    typ = str(card.type_line())
    while "Creature" not in typ:
        card = scrython.cards.Random()
        typ = str(card.type_line())
    return typ

def generate_card():
    descIndex = random.randint(0, 3)
    desc = ""
    CARDNAME = rand_name()
    card_type = get_creature_type_line()
    match descIndex:
        case 0:
            desc = (rand_add("creature", "rand") + "\nWhenever you " + rand_player_trigger().lower() + ", " + rand_effect().lower())
        case 1:
            desc = (rand_add("creature", "rand") + "\n" + rand_ct() + "s you control have " + rand_add("creature", "1") + ".")
        case 2:
            desc = (rand_add("creature", "rand") + "\nWhenever " + CARDNAME + " " + rand_permanent_trigger().lower() + ", " + rand_effect().lower())
        case 3:
            desc = (rand_add("creature", "rand") + "\n" + rand_noun() + "s can't " + rand_permanent_trigger().lower())

    mana_cost = rand_mana_cost()
    card = Card(CARDNAME, card_type, mana_cost, desc, rand_rarity(), rand_pnt(mana_cost))
    return card

print (generate_card().to_string())

while(True):
    cont = input()
    print (generate_card().to_string())




