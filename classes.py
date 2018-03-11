class Character(object):
#Default class for any living thing
    def __init__(self, health, armor, strength, gold):
        self.name = ''
        self.health = health
        self.armor = armor
        self.strength = strength
        self.gold = gold
    def print_data(self):
        print('Name: {}\nHealth: {}  Armor: {}  Strength: {}'.format(self.name,self.health,self.armor,self.strength))

class Human(Character):
#Represents the human player in the game
    def __init__(self, health, armor, strength, gold):
        Character.__init__(self, health, armor, strength, gold)
        self.name = input("Please enter your name > ")
        self.experience = 0
        self.weapon = Weapon("No weapon equipped", 0,0)

class Enemy(Character):
#Represents the enemy player in the game
    def __init__(self, name, health, armor, strength, experience, gold, index):
        Character.__init__(self, health, armor, strength, gold)
        self.name = name
        self.experience = experience
        self.index = index

class Item(object):
#Represents any item in the game
    def __init__(self, name, hvalue, armvalue, strvalue, cost):
        self.name = name
        self.hvalue = hvalue
        self.armvalue = armvalue
        self.strvalue = strvalue
        self.cost = cost

class Weapon(Item):
#Weapon shorthand initializes Item with armor and health values set to 0
    def __init__(self, name, strvalue, cost, index):
        Item.__init__(self, name, 0, 0, strvalue, cost)
        self.index = index

class Layer(object):
    def __init__(self, name, lore, attack_frequency , monster_index, index):
        self.name = name
        self.lore = lore
        self.attack_frequency = attack_frequency
        self.monster_index = monster_index
        self.index = index