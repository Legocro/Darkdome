import sys, time, random
from classes import Enemy, Weapon, Layer
from random import randint
def SpawnMonster(index):
    with open("Text_files/Monsters.txt") as file:
        raw_data = file.read()
        arr = raw_data.split("\n")
        monster_index = randint(0, index)
        monster_arr = arr[monster_index].split(",")
        monster_name = monster_arr.pop(0)
        monster_data = map(int, monster_arr)
        return Enemy(monster_name, *monster_data)
def GetWeapon(index):
    with open("Text_files/Weapons.txt") as file:
        raw_data = file.read()
        arr = raw_data.split("\n")
        weapon_arr = arr[index].split(",")
        weapon_name = weapon_arr.pop(0)
        weapon_data = map(int, weapon_arr)
        return Weapon(weapon_name, *weapon_data)
def GetLayer(index):
    with open("Text_files/Layers.txt") as file:
        raw_data = file.read()
        arr = raw_data.split("\n")
        layer_arr = arr[index].split("|")
        layer_name = layer_arr.pop(0)
        layer_lore = layer_arr.pop(0)
        layer_data = map(int, layer_arr)
        return Layer(layer_name, layer_lore, *layer_data)
def slow_type(t,speed):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/speed)
    print ("")

slow_type("Yo what's up, I'm lego, how's it going", typing_speed)