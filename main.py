#Dark Dome

#Import required modules
import jsonpickle, os, sys, time
from classes import AI, Human, Item
from util import SpawnMonster
from random import randint
#main game

#Variables
go = True
IsShopLocked = False
IsWeaponEquipped = False
IsShieldEquipped = False
IsArmorEquipped = False
IsDaggerEquipped = False
IsSwordEquipped = False
IsScimitarEquipped = False
IsLongswordEquipped = False
IsLeatherHideEquipped = False
SAVEGAME_FILENAME = 'DDSave.json'
game_state = dict()

###functions for loading, saving, and initializing the game###
def load_game():
    """Load game state from a predefined savegame location and return the
    game state contained in that savegame.
    """
    with open(SAVEGAME_FILENAME, 'r') as savegame:
        state = jsonpickle.decode(savegame.read())
    return state


def save_game():
    """Save the current game state to a savegame in a predefined location.
    """
    
    with open(SAVEGAME_FILENAME, 'w') as savegame:
        savegame.write(jsonpickle.encode(game_state))


def initialize_game():
    """If no savegame exists, initialize the game state with some
    default values.
    """
    
    player = Human(100, 10, 10, 0)

    state = dict()
    state['players'] = [player]
    return state

###End functions for loading, saving, and initalizing the game###

###Main game functions###
#Function for the shop
def Shop():
    global IsDaggerEquipped
    global IsSwordEquipped
    global IsScimitarEquipped
    global IsLongswordEquipped
    global game_state
    player = game_state['players'][0]
    dagger = Item('Dagger', 0, 0, 10)
    sword = Item('Sword', 0, 0, 15)
    scimitar = Item('Scimitar', 20, 0, 43)
    longsword = Item('Longsword', 50, 40, 96)
    leather_hide = Item('Leather Hide', 5, 5, 0)
    if IsShopLocked == True:
        print("The shop is locked!\nPlease go back and continue your adventure!")
    else:
        print()
        print("Welcome to the Dome shop! What would you like to buy?\n1. Weapons\n2. Armor\n3. Go back")
        selection = int(input("Enter a value: "))

    if selection == 1:
        print("Weapons shop")
        print("1. Bronze Dagger: $20\n2. Bronze Sword: $50\n3. Bronze Scimitar: $100\n4. Bronze Longsword: $1.000")
        wpnselection = int(input("Enter a value: "))

        if wpnselection == 1:
            if IsDaggerEquipped == True:
                print("You already have this weapon equipped...")
                Game_Loop()
            else:
                dagger = Item('Dagger', 0, 0, 10)
                IsDaggerEquipped = True
                player.strength += dagger.strvalue
                player.gold -= 20
                print("strength increased to: {}".format(player.strength))
                Game_Loop()

        elif wpnselection == 2:
            if IsSwordEquipped == True:
                print("You already have this weapon equipped...")
                Game_Loop()
            elif IsDaggerEquipped == False:
                print("You should get a dagger first...")
                Game_Loop()
            else:
                sword = Item('Sword', 0, 0, 22)
                IsSwordEquipped = True
                IsDaggerEquipped = False
                player.strength += sword.strvalue
                player.strength -= dagger.strvalue
                player.gold -= 50
                print("strength increased to: {}".format(player.strength))
                Game_Loop()

        elif wpnselection == 3:
            
            if  IsScimitarEquipped == True:
                print("You already have this weapon equipped...")
                Game_Loop()
            elif IsSwordEquipped == False:
                print("You should get a sword first...")
                Game_Loop()
            else:
                scimitar = Item('Scimitar', 25, 0, 43)
                IsScimitarEquipped = True
                IsSwordEquipped = False
                player.health += scimitar.hvalue
                player.strength += scimitar.strvalue
                player.strength -= sword.strvalue
                player.gold -= 100
                print("strength increased to: {}".format(player.strength))
                Game_Loop()
         
        elif wpnselection == 4:
            
            if  IsLongswordEquipped == True:
                print("You already have this weapon equipped...")
                Game_Loop()
            elif IsScimitarEquipped == False:
                print("You should get a scimitar first...")
                Game_Loop()
            else:
                longsword = Item('Longsword', 50, 40, 96)
                IsLongswordEquipped = True
                IsScimitarEquipped = False
                player.strength += longsword.strvalue
                player.strength -= scimitar.strvalue
                player.gold -= 1000
                print("strength increased to: {}".format(player.strength))
                Game_Loop()
            
        elif wpnselection == 5:
            Game_Loop()

    elif selection == 2:
        if player.gold >= 20:
            print ("Armor Shop")
            print ("1. Leather hide\n2. Bronze Shield")
            armselection = int(input("enter a value: "))

        if armselection == 1:
            global IsLeatherHideEquipped
            if IsLeatherHideEquipped == True:
                print("You are already wearing armor!")
                Game_Loop()
            else:
                leather_hide = Item('Leather Hide', 5, 5, 0)
                IsLeatherHideEquipped = True
                player.health += leather_hide.hvalue
                player.gold -= 20
                print("Health increased to: {}".format(player.health))
                Game_Loop()

        if armselection == 2:
            global IsShieldEquipped
            if IsShieldEquipped == True:
                print("You are already caryying a shield!")
                Game_Loop()
            else:
                bronze_shield = Item('Bronze Shield', 0, 10, 0)
                IsShieldEquipped = True
                player.armor += bronze_shield.armvalue
                player.gold -= 30
                print("Armor increased to: {}".format(player.armor))
                Game_Loop()

        elif armselection == 3:
            Game_Loop()

    elif selection == 4:
        Game_Loop()

#Function for combat
def Combat():
    global game_state
    player = game_state['players'][0]
    enemy = SpawnMonster(randint (1, 17))
    global go
    while go == True:
        pdmg = randint (0, player.strength)
        edmg = randint (0, enemy.strength)
        enemy.health -= pdmg

        if player.health <= 0:
            os.system('cls')
            print()
            print("You have been pwnd by a mere {}...".format(enemy.name))
            #go = False
            leave = input("press enter to exit")
            Game_Loop()

        elif enemy.health <= 0:
            os.system('cls')
            player.gold += enemy.gold
            print()
            print("You have received {}!".format(enemy.gold) + " Gold")
            print()
            print("You have valorously slain the  {}!".format(enemy.name))
            #go = False
            leave = input("press any key to exit")
            Game_Loop()

        else:
            os.system('cls')
            with open("test.txt", "r") as in_file:
                text = in_file.read()
            print(text)
            enemy.print_data()
            player.health -= edmg
            print()
            print("You attack the enemy {} and deal {} damage!".format(enemy.name, pdmg))
            print("The enemy has {} health left!".format(enemy.health))
            print()
            print("The enemy {} attacks you for {} damage!".format(enemy.name, edmg))
            print("You have {} health left!".format(player.health))
            time.sleep(3)

#The main game loop
def Game_Loop():
    global game_state
    while True:
        print()
        print("You are currently in front of the Dark Dome!")
        print("What would you like to do?")
        print("1. Shop\n2. Enter the Dark Dome!\n3. View player statistics\n4. Save game. \n5. Exit game.")
        print()
        try:
            selection = int(input("Enter a value: "))
        except ValueError:
            print()
            print("You can only use number input.")
            print()
            Game_Loop()
        if selection == 1:
            Shop()
        elif selection == 2:
            Combat()
        elif selection == 3:
            player = game_state['players'][0]            
            print()
            print("Your players stats:\nHealth: {}\nArmor: {}\nStrength: {}\nGold: {}".format(player.health, player.armor, player.strength, player.gold))
            if IsDaggerEquipped == True:
                print("You have a dagger equipped")
            elif IsSwordEquipped == True:
                print ("You have a sword equipped")
            elif IsLeatherHideEquipped == True:
                print("You are wearing a leather hide")
            elif IsShieldEquipped == True:
                print ("You have a shield equipped")
        elif selection == 4:
            save_game()
        elif selection == 5:
            print("Exiting game...")
            exit()
        else:
            print()
            print("Oops! Not a valid input")
            print()

###End main game functions###

###The "main" function, not to be confused with anything to do with main above it###
def main():
    """Main function. Check if a savegame exists, and if so, load it. Otherwise
    initialize the game state with defaults. Finally, start the game.
    """
    global game_state
    if not os.path.isfile(SAVEGAME_FILENAME):
        game_state = initialize_game()
    else:
        game_state = load_game()
    Game_Loop()


if __name__ == '__main__':
    main()

###end main function###
