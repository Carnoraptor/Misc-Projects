import scrython

# guess the set a card is from

points = 0

def play1():
    print("\n \n")
    global points
    card = scrython.cards.Random()
    desc = card.oracle_text().replace(card.name(), "CARDNAME")
    print("This card is a " + card.type_line() + " that costs " + card.mana_cost() + ". The description of this card is: " + desc)
    
    playerInp = input("What is the name of this card?")
    if (playerInp.lower() == card.name().lower()):
        points += 3
        print("Nice, exactly right!! You have " + str(points) + " points!");
        play1()
    elif((playerInp.lower() in card.name().lower()) and len(playerInp) >= 3):
        points += 1
        print("Good job, that's in the name! The full name is " + card.name() + ". You have " + str(points) + " points!")
        play1()
    else:
        points -= 1
        print("That's incorrect. The correct answer is " + card.name() + ". You have " + str(points) + " points.")
        play1()


def play3():
    print("\n \n")
    global points
    card = scrython.cards.Random()
    desc = card.oracle_text().replace(card.name(), "CARDNAME")
    print("This card is a " + card.type_line() + " from " + card.set_name() + ". The description of this card is: " + desc)
    
    playerInp = input("What is the color of this card?")
    if (list(playerInp.lower()).sort() == (list("".join(card.colors()).lower())).sort()):
        points += 1
        print("Nice, exactly right!! The card is " + card.name() + ". You have " + str(points) + " points!")
        play3()
    elif(playerInp.lower() in "".join(card.colors()).lower()):
        points += 0
        print("Good job, that's one of the colors! The card is " + card.name() + " and it's " + "".join(card.colors()) + ". You have " + str(points) + " points!")
        play3()
    else:
        points -= 1
        print("That's incorrect. The card is " + card.name() + " and it's " + "".join(card.colors()) + ". You have " + str(points) + " points.")
        play3()

print("Welcome to MTGuessr! Time to test your knowledge of Magic through a few \n possible options!")

print("To guess based on rules text, press 1. \nTo guess based on card art, press 2. \nTo guess the color of a card, press 3.")
gamemode = input("")

if (gamemode == "1"):
    play1()
elif(gamemode == "2"):
    play2()
else:
    play3()
