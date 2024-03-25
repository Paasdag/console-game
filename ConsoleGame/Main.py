# imports
import random
from cfg.cfg import *
from Armor import *
from boss import *
# vars
player_health = 20
armor_boots = ""
armor_legs = ""
armor_chestplate = ""
armor_helmet = ""
sword = ""
sword_dmg_boost = 0
lvl = int("1")

print(f"Hello, this is an grind game developed by" + Made_by)
print(f"Version: " + version)
inpt_1 = input("Would you like to recive an starter kit (y / n): ")
answer_1 = inpt_1.lower()
if answer_1 == "y":
    armor_negitive = 1.2
    armor_boots = "Starter boots"
    armor_legs = "Starter legs"
    armor_chestplate = "Starter chestplate"
    armor_helmet = "Starter helmet"
    sword = "Starter sword"
    sword_dmg_boost = 1.5
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
                if boss_inpt1 == "attack":
                    boss_dmg = random.randint(3,5)
                    boss_dmg_calc = boss_dmg / armor_negitive
                    take_health = player_health / boss_dmg_calc
                    print(player_health)
                    player_dmg = random.randint(5,10)
                    player_dmg_calc = player_dmg * sword_dmg_boost
                    print(player_dmg_calc)
    else: 
        if default_answer != "armor" or "command":
            print("Not a default answer")
