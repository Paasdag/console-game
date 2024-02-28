# imports
from cfg.cfg import *
from Armor import *
from boss import *
# vars
armor_boots = ""
armor_legs = ""
armor_chestplate = ""
armor_helmet = ""
sword = ""
lvl = int("1")

print(f"Hello, this is an grind game developed by" + Made_by)
print(f"Version: " + version)
inpt_1 = input("Would you like to recive an starter kit (y / n): ")
answer_1 = inpt_1.lower()
if answer_1 == "y":
    armor_boots = "Starter boots"
    armor_legs = "Starter legs"
    armor_chestplate = "Starter chestplate"
    armor_helmet = "Starter helmet"
    sword = "Starter sword"
    print("Starter kit recived")
if answer_1 != "y":
    print("Starter kit not recived")
# default input and stuff
while True:
    default_inpt = input("Actions possible -> armor, figth : ")
    default_answer = default_inpt.lower()
    if default_answer == "armor":
        print(f"Helmet: " + armor_helmet + " Legs: " + armor_legs + " Chestplate: " + armor_chestplate + " helmet: " + armor_helmet)
    if default_answer == "figth":
        if lvl == 1:
            print("Lvl 1 boss")
            print("Recomended gear: none or starter")
            inpt_2 = input("Want to continue (y/n): ")
            answer_2 = inpt_2.lower()
            if answer_2 == 'y':
                print("\033[2J\033[H", end="", flush=True)
                print("Simple boss: health -> 25")
                boss_inpt1 = input("Options: Attack, Return: ")
                if boss_inpt1 == "Attack":
                    print("WIP")
    else: 
        if default_answer != "armor" or "command":
            print("Not a default answer")