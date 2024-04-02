# imports test
import random
from cfg.cfg import *
from Armor.armor import *
from boss.simple_boss import *
print(boss_health)
# vars
player_health = 20
player_health_max = 20
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
    SetArmor("Starter Helmet", "Starter Chestplate", "Starter leggings", "Starter boots", "1.2")
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
                    # wip
                    boss_dmg_calc = boss_dmg / armor_negitive
                    take_health = player_health / boss_dmg_calc
                    player_health = player_health - take_health
                    print("the boss has done", take_health, "damage")
                    player_dmg = random.randint(5,10)
                    player_dmg_calc = player_dmg * sword_dmg_boost
                    print("you have done", player_dmg_calc, " damage to the lvl 1 boss")
                    if boss_health == 0:
                        print("You have succsesfully killed the boss")
                        player_health = player_health_max
                    if player_health == 0:
                        print("You have died. Good news you dont lose anything")
                        player_health = player_health_max
                    
    else: 
        if default_answer != "armor" or "figth":
            print("Not a default answer")
