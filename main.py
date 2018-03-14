#Dark Dome

#Import required modules
import jsonpickle, os, sys, time
from classes import Human, Item, Layer
from util import SpawnMonster, GetWeapon, GetLayer
from random import randint
#main game

#Variables
go = True
IsShopLocked = False
IsWeaponEquipped = False
IsShieldEquipped = False
IsArmorEquipped = False
IsLeatherHideEquipped = False
time_since_attack = time.clock()
layer = GetLayer(0)
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

    global game_state
    player = game_state['players'][0]
    
    leather_hide = Item('Leather Hide', 5, 5, 0,0)
    if IsShopLocked == True:
        print("The shop is locked!\nPlease go back and continue your adventure!")
    else:
        print()
        print("Welcome to the Dome shop! What would you like to buy?\n1. Weapons\n2. Armor\n3. Go back")
        print('\033[0;35m', end="")
        selection = int(input("Enter a value: "))

    if selection == 1:
        print("Weapons shop")
        global IsWeaponEquipped
        if not IsWeaponEquipped:
            weapon = GetWeapon(0)
        else:
            weapon = GetWeapon(player.weapon.index + 1)
        print("1. {!s} - {} gold\n3. Go back.".format(weapon.name, weapon.cost))
        wpnselection = int(input("Enter a value: "))

        if wpnselection == 1 and player.gold >= weapon.cost:
            player.gold -= weapon.cost
            player.strength += weapon.strvalue
            player.weapon = weapon
            IsWeaponEquipped = True
            print("strength increased to: {}".format(player.strength))
            Game_Loop()
        elif wpnselection == 2:
            Game_Loop()
        else:
            print("Not enough gold.")
            time.sleep(2)

    elif selection == 2:
        if player.gold >= 20:
            print ("Armor Shop")
            print ("1. Leather hide\n2. Bronze Shield")
            armselection = int(input("enter a value: "))
        else:
            print("Not enough gold.")
            time.sleep(2)
            Game_Loop()
        if armselection == 1:
            global IsLeatherHideEquipped
            if IsLeatherHideEquipped == True:
                print("You are already wearing armor!")
                Game_Loop()
            else:
                leather_hide = Item('Leather Hide', 5, 5, 0, 0)
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
                bronze_shield = Item('Bronze Shield', 0, 10, 0, 0)
                IsShieldEquipped = True
                player.armor += bronze_shield.armvalue
                player.gold -= 30
                print("Armor increased to: {}".format(player.armor))
                Game_Loop()

        elif armselection == 3:
            Game_Loop()

    elif selection == 4:
        Game_Loop()

#Function for 'playing' a layer
def PlayLayer(layer):
    while True:
        os.system('cls')
        print(layer.lore)
        print("\n")
        print("1. Go up.")
        if layer.index > 0:
            print("2. Go down.")
        else:
            print("2. Go out.")
        if time.clock() - time_since_attack >= layer.attack_frequency:
            enemy = SpawnMonster(layer.index)
            Combat(enemy, layer)
        selection = int(input("Enter a value: "))
        if selection == 1:
            PlayLayer(GetLayer(layer.index+1))
        elif selection == 2:
            Game_Loop()

#Function for combat
def Combat(enemy, layer):
    global game_state
    player = game_state['players'][0]
    while True:
        #Idk, nesto sam mislio tu, ali mi se nije dalo napravit do kraja ovo
        if enemy.armor > player.strength:
            pdmg = 0
        else:
            pdmg = randint (0, player.strength)
        edmg = randint (0, enemy.strength)
        enemy.health -= pdmg

        if player.health <= 0:
            os.system('cls')
            print()
            print("You have been pwnd by a mere {!s}...".format(enemy.name))
            #go = False
            input("press enter to exit")
            Game_Loop()

        elif enemy.health <= 0:
            os.system('cls')
            player.gold += enemy.gold
            print()
            print("You have received {}".format(enemy.gold) + " Gold")
            print()
            print("You have valorously slain the  {!s}!".format(enemy.name))
            #go = False
            time.sleep(3)
            global time_since_attack
            time_since_attack = time.clock()
            PlayLayer(layer)
        else:
            os.system('cls')
            print("You are attacked by an enemy on {}".format(layer.name))
            enemy.print_data()
            player.health -= edmg
            print()
            print("You attack the enemy and deal {} damage!".format(pdmg))
            print("The enemy has {} health left!".format(enemy.health))
            print()
            print("The enemy attacks you for {} damage!".format(edmg))
            print("You have {} health left!".format(player.health))
            if player.health > 0:
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
            PlayLayer(layer)
        elif selection == 3:
            player = game_state['players'][0]            
            print()
            print("Your players stats:\nHealth: {}\nArmor: {}    Weapon: {}\nStrength: {}\nGold: {}".format(player.health, player.armor, player.weapon.name, player.strength, player.gold))
            if IsLeatherHideEquipped == True:
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
