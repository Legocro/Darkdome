with open("Text_files/Weapons.txt") as file:
    raw_data = file.read()
    arr = raw_data.split("\n")
    weapon_arr = arr[index].split(",")
    weapon_name = weapon_arr.pop(0)
    weapon_data = map(int, weapon_arr)
    return Weapon(weapon_name, *weapon_data)