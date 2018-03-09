import sys
from classes import AI
from random import randint
def SpawnMonster(index):
    with open("MON.txt") as file:
        raw_data = file.read()
        arr = raw_data.split("\n")
        arr.pop()
        monster_index = randint(0, index)
        monster_arr = arr[0].split(",")
        monster_name = monster_arr.pop(0)
        monster_data = map(int, monster_arr)
        return AI(monster_name, *monster_data)

