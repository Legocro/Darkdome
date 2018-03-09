
class Character(object):
#Default class for any living thing
    def __init__(self, health, armor, strength):
        self.name = ''
        self.health = health
        self.armor = armor
        self.strength = strength
    def print_data(self):
        print('Name: {}\nHealth: {}  Armor: {}  Strength: {}'.format(self.name,self.health,self.armor,self.strength))

class Human(Character):
#Represents the human player in the game
    def __init__(self, health, armor, strength, gold):
        Character.__init__(self, health, armor, strength, gold)
        self.name = input("Please enter your name > ")
        self.health = health
        self.armor = armor
        self.strength = strength
        self.gold = gold

class AI(Character):
#Represents the enemy player in the game
    def __init__(self, name, health, armor, strength, experience, gold, index):
        Character.__init__(self, health, armor, strength)
        self.name = name
        self.health = health
        self.armor = armor
        self.strength = strength
        self.gold = gold
        self.experience = experience
        self.index = index

class Item(object):
#represents any item in the game
    def __init__(self, name, hvalue, armvalue, strvalue):
        self.name = name
        self.hvalue = hvalue
        self.armvalue = armvalue
        self.strvalue = strvalue
