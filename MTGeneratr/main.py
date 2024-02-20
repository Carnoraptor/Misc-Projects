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
         "Is transformed",
         "Is exiled",
         "Untaps",
         "Becomes blocked",
         "Attacks",
         "Attacks the player with the most life",
         "Attacks the player with the least life",
         "Has a counter placed on it",
         "Fights",
         "Create"
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
         "Create a NOUN token"
         "Target NOUN gets ADD until end of turn",]
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
         "Blood token",
         "Clue token",
         "Food token",
         "Treasure token",
         "Card",]
additions = ["Affinity for NOUN",
             "NOUNcycling RANDMANA",
             "Kicker RANDMANA",
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
             "Flash",
             "Hexproof",
             "Indestructible",
             "Lifelink",
             "Ward RANDMANA",
             "Fear",]


class Card:
    name = "CardName"
    manaCost = "4R"
    description = ""
    rarity = "C"

    def __init__(self, _name, _manaCost, _description, _rarity):
        self.name = _name
        self.manaCost = _manaCost
        self.description = _description
        self.rarity = _rarity

    def to_string(self):
        return "Name: " + self.name + "\nMana Cost: " + self.manaCost + "\nDescription: " + self.description + "\nRarity: " + self.rarity;


def parse_string(_string):
    string = _string
    string = string.replace("NOUN", str(nouns[random.randint(0, len(nouns) - 1)]).lower())
    string = string.replace("ADD", str(additions[random.randint(0, len(nouns) - 1)]).lower())
    string = string.replace("RANDMANA", "{" + rand_mana_cost() + "}")
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

def rand_add():
    return parse_string(additions[random.randint(0, len(additions) - 1)])

def rand_mana_cost():
    card = scrython.cards.Random()
    return card.mana_cost().lower()

def rand_rarity():
    rarities = ["Common", "Uncommon", "Rare", "Mythic Rare"]
    return rarities[random.randint(0, 3)]


def generate_card():
    descIndex = random.randint(0, 3)
    desc = ""
    CARDNAME = "CARDNAME"
    match descIndex:
        case 0:
            desc = (rand_add() + ", " + rand_add().lower() + "\nWhenever you " + rand_player_trigger().lower() + ", " + rand_effect().lower())
        case 1:
            desc = (rand_add() + "\nIf you would " + rand_player_trigger().lower() + ", instead " + rand_effect().lower())
        case 2:
            desc = (rand_add() + "\nWhenever " + CARDNAME + " " + rand_permanent_trigger().lower() + ", " + rand_effect().lower())
        case 3:
            desc = (rand_add() + "\n" + rand_noun() + "s can't " + rand_permanent_trigger().lower())

    card = Card(CARDNAME, rand_mana_cost(), desc, rand_rarity())
    return card

print (generate_card().to_string())

while(True):
    cont = input()
    print (generate_card().to_string())







    
