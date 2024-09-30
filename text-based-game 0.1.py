import sys
import random
import time
x = 1
z = 0
y = 0
e = 0
r = 0
t = 0
u = 0
i = 0
m = 0
coins = 500
gearscore = 0
simple_essence = 0
undead_essence = 0
simple_fragments = 0
dungeon_upgrade = 0
amount = 0
addcoins = 0
addsimple_essence = 0
addundead_essence = 0
number = 0
dungeon_score = 0

gear = ["simple dagger", "cloth headwrap", "cloth tunic", "cloth pants", "cloth shoes", "leather cap", "leather tunic", "leather pants", "leather boots", "undead helmet", "stone club", "simple saber", "simple shield", "claw talisman"]
score = [5, 3, 5, 4, 3, 5, 7, 6, 4, 8, 7, 10, 5, 2]
price = [100, 40, 65, 50, 35, 70, 100, 85, 55, 150, 150, 220, 100, 120]
amount = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
equipped = [False, False, False, False, False, False, False, False, False, False, False, False, False, False,]
short = ["sd", "ch", "ct", "cp", "cs", "lc", "lt", "lp", "lb", "uh", "sc", "ss", "ssh", "cta"]


while x == 1:
    print("you currently have the following items:")
    for i in range (0, 14):
        if amount[i] > 0:
            print(gear[i] + ": " + str(amount[i]) + "x " + "gearscore: " + str(score[i]))

    print("you currently have these items equipped:")
    for i in range (0,14):
        if equipped[i] == True:
            print(gear[i] + ": " + "gearscore: " + str(score[i]))
            
    print("you currently have " + str(gearscore) + " gearscore")
    print("you currently have " + str(coins) + " coins")
    print("")
    print("what do you want to do ?")
    print("(1) change equip")
    print("(2) sell equip")
    print("(3) upgrade equip")
    print("(4) enter dungeon")
    print("(5) salvage equip")
    print("(6) enter essence shop")
    print("(7) view loot tables")
    print("(8) exit the game")
    print("(9) view tutorial")
    print("(10) the vault")
    
    player_input = (input())
    if player_input == "1":
        
        print("you currently have the following equip:")
        for i in range (0, 14):
            if amount[i] > 0:
                print(gear[i] + ": " + str(amount[i]) + "x " + "gearscore: " + str(score[i]))
        print("")
            
        print("you have the following items equipped")
        for i in range (0,14):
            if equipped[i] == True:
                print(gear[i] + ": " + "gearscore: " + str(score[i]))
        print("")
        
        print("what do you want to do?")
        print("(1) add equip")
        print("(2) remove equip")
        
        player_input = (input())
        if player_input == "1":
            
            print("you have the following equip:")
            for i in range (0,14):
                if amount[i] > 0:
                    print(gear[i] + ": " + str(amount[i]) + "x " + "gearscore: " + str(score[i]) + "short: " + short[i])
                    
            print("which item do you want to equip?")
            player_input = (input())
            for i in range (0,14):
                if player_input == short[i] and i != 3 and i != 7:
                    if amount[i] > 0:
                        gearscore = gearscore + score[i]
                        equipped[i] = True
                    else:
                        print("you don't have this item")
                elif player_input == short[3] and equipped[3] == False and equipped[7] == False:
                    if amount[i] > 0:
                        print("you have equipped your " + gear[3])
                        gearscore == gearscore + score[3]
                        equipped[3] = True
                    else:
                        print("you don't have this item")
                elif player_input == short[7] and equipped[3] == False and equipped[7] == False:
                    if amount[i] > 0:
                        print("you have equipped your " + gear[7])
                        gearscore == gearscore + score[7]
                        equipped[7] = True
                    else:
                        print("you don't have this item")
                        
                if player_input == short[i] and i != 1 and i != 5 and i != 9:
                    if amount[i] > 0:
                        gearscore = gearscore + score[i]
                        equipped[i] = True
                    else:
                        print("you don't have this item")
                elif player_input == short[1] and equipped[1] == False and equipped[5] == False and equipped[9] == False:
                    if amount[i] > 0:
                        print("you have equipped your " + gear[1])
                        gearscore == gearscore + score[1]
                        equipped[1] = True
                    else:
                        print("you don't have this item")
                elif player_input == short[5] and equipped[5] == False and equipped[1] == False and equipped[9] == False:
                    if amount[i] > 0:
                        print("you have equipped your " + gear[5])
                        gearscore == gearscore + score[5]
                        equipped[5] = True
                    else:
                        print("you don't have this item")
                elif player_input == short[9] and equipped[9] == False and equipped[1] == False and equipped[5] == False:
                    if amount[i] > 0:
                        print("you have equipped your " + gear[9])
                        gearscore == gearscore + score[9]
                        equipped[9] = True
                    else:
                        print("you don't have this item")
                
                if player_input == short[i] and i != 0 and i != 10 and i != 11:
                    if amount[i] > 0:
                        gearscore = gearscore + score[i]
                        equipped[i] = True
                    else:
                        print("you don't have this item")
                elif player_input == short[0] and equipped[0] == False and equipped[10] == False and equipped[11] == False:
                    if amount[i] > 0:
                        print("you have equipped your " + gear[0])
                        gearscore == gearscore + score[0]
                        equipped[0] = True
                    else:
                        print("you don't have this item")
                elif player_input == short[10] and equipped[10] == False and equipped[11] == False and equipped[0] == False:
                    if amount[i] > 0:
                        print("you have equipped your " + gear[10])
                        gearscore == gearscore + score[10]
                        equipped[10] = True
                    else:
                        print("you don't have this item")
                elif player_input == short[11] and equipped[11] == False and equipped[10] == False and equipped[0] == False:
                    if amount[i] > 0:
                        print("you have equipped your " + gear[11])
                        gearscore == gearscore + score[11]
                        equipped[11] = True
                    else:
                        print("you don't have this item")
                
                if player_input == short[i] and i != 2 and i != 6:
                    if amount[i] > 0:
                        gearscore = gearscore + score[i]
                        equipped[i] = True
                    else:
                        print("you don't have this item")
                elif player_input == short[2] and equipped[2] == False and equipped[6] == False:
                    if amount[i] > 0:
                        print("you have equipped your " + gear[2])
                        gearscore == gearscore + score[2]
                        equipped[2] = True
                    else:
                        print("you don't have this item")
                elif player_input == short[6] and equipped[6] == False and equipped[2] == False:
                    if amount[i] > 0:
                        print("you have equipped your " + gear[6])
                        gearscore == gearscore + score[6]
                        equipped[6] = True
                    else:
                        print("you don't have this item")
                
                if player_input == short[i] and i != 4 and i != 8:
                    if amount[i] > 0:
                        print("you have equipped your " + gear[i])
                        gearscore = gearscore + score[i]
                        equipped[i] = True
                    else:
                        print("you don't have this item")
                elif player_input == short[4] and equipped[4] == False and equipped[8] == False:
                    if amount[i] > 0:
                        print("you have equipped your " + gear[4])
                        gearscore == gearscore + score[4]
                        equipped[4] = True
                    else:
                        print("you don't have this item")
                elif player_input == short[8] and equipped[8] == False and equipped[4] == False:
                    if amount[i] > 0:
                        print("you have equipped your " + gear[8])
                        gearscore == gearscore + score[8]
                        equipped[8] = True
                    else:
                        print("you don't have this item")
            print("")
            print("-----------------------------------------------------------------------------------------------")
                
                
        if player_input == "2":
            
            print("you have the following items equipped")
            for i in range (0,14):
                if equipped[i] == True:
                    print(gear[i] + ": " + "gearscore: " + str(score[i]))
            print("")
            print("which item do you want to unequip?")
            
            player_input = (input())
            for i in range (0,14):
                if equipped[i] == True and player_input == short[i]:
                    gearscore = gearscore + score[i]
                    amount[i] = amount[i] + 1
                    equipped[i] = False
                    print("you have unequipped your " + gear[i])
            print("")
            print("----------------------------------------------------------------------------")
            
                
    elif player_input == "2":
        print("what items do you want to sell?")
        print("you have the following items:")
        for i in range (0,14):
            if amount[i] > 0:
                print(gear[i] + ": " + str(amount[i]) + " x " + "price: " + str(price[i]) + " short: " + short[i])
        
        player_input = str(input())
        for i in range (0,14):
            if player_input == short[i] and amount > 0:
                print("you have sold your " + gear[i] + " for " + str(price[i]) + " coins")
                amount[i] = amount[i] - 1
                coins = coins + price[i]
                print("you now have " + str(coins) + " coins!")
                print("")
                print("-------------------------------------------------------------------------")
                
        
        
        
        
    
    
    elif player_input == "3":
        print("the developer is currently too lazy to develop this")
        print("what items do you want to upgrade?")
        time.sleep (2)
        print("seriously there's nothing here")
        time.sleep (3)
        print("go< there's nothing to see here")
        time.sleep (5)
        print("why are you still here???????")
        time.sleep (10)
        print("ok, ok the code is hiddenwaffles")
        print("")
        print("-----------------------------------------------------------------------------------")
    
    
    elif player_input == "4":
        print("which floor do you want to enter?")
        print("(1) floor 1 (recommended gearscore: 20)")
        print("(2) floor 2 (recommended gearscore: 40)")
        print("(3) floor 3 (recommended gearscore: 70)")
        print("(4) floor 4 (recommended gearscore: 120)")
        print("(5) floor 5 (recommended gearscore: 200)")
        print("(6) floor 6 (recommended gearscore: 350)")
        print("(7) floor 7 (recommended gearscore: 600)")
        print("Maximum score for all dungeons is 300!")
        player_input = (input())
        if player_input == "1":
            print("you entered floor 1")
            for n in range ( 1,11 ):
                print(n)
                time.sleep(1)
            if gearscore == 0:
                dungeon_score = random.randrange(1,16)
            if gearscore == 1:
                dungeon_score = random.randrange(1,31)
            if gearscore == 2:
                dungeon_score = random.randrange(5,38)
            if gearscore == 3:
                dungeon_score = random.randrange(11,43)
            if gearscore == 4:
                dungeon_score = random.randrange(20,51)
            if gearscore == 5:
                dungeon_score = random.randrange(26,61)
            if gearscore == 6:
                dungeon_score = random.randrange(31,70)
            if gearscore == 7:
                dungeon_score = random.randrange(36,79)
            if gearscore == 8:
                dungeon_score = random.randrange(41,88)
            if gearscore == 9:
                dungeon_score = random.randrange(51,101)
            if gearscore == 10:
                dungeon_score = random.randrange(56,121)
            if gearscore == 11:
                dungeon_score = random.randrange(61,136)
            if gearscore == 12:
                dungeon_score = random.randrange(66,151)
            if gearscore == 13:
                dungeon_score = random.randrange(71,161)
            if gearscore == 14:
                dungeon_score = random.randrange(76,171)
            if gearscore == 15:
                dungeon_score = random.randrange(81,181)
            if gearscore == 16:
                dungeon_score = random.randrange(86,191)
            if gearscore == 17:
                dungeon_score = random.randrange(91,201)
            if gearscore == 18:
                dungeon_score = random.randrange(96,211)
            if gearscore == 19:
                dungeon_score = random.randrange(101,226)
            if gearscore == 20:
                dungeon_score = random.randrange(111,241)
            if gearscore == 21:
                dungeon_score = random.randrange(121,256)
            if gearscore == 22:
                dungeon_score = random.randrange(131,271)
            if gearscore == 23:
                dungeon_score = random.randrange(141,281)
            if gearscore == 24:
                dungeon_score = random.randrange(151,291)
            if gearscore == 25:
                dungeon_score = random.randrange(156,301)
            if gearscore == 26:
                dungeon_score = random.randrange(161,301)
            if gearscore == 27:
                dungeon_score = random.randrange(166,301)
            if gearscore == 28:
                dungeon_score = random.randrange(171,301)
            if gearscore == 29:
                dungeon_score = random.randrange(176,301)
            if gearscore == 30:
                dungeon_score = random.randrange(181,301)
            if gearscore == 31:
                dungeon_score = random.randrange(186,301)
            if gearscore == 32:
                dungeon_score = random.randrange(191,301)
            if gearscore == 33:
                dungeon_score = random.randrange(196,301)
            if gearscore == 34:
                dungeon_score = random.randrange(201,301)
            if gearscore == 35:
                dungeon_score = random.randrange(206,301)
            if gearscore == 36:
                dungeon_score = random.randrange(211,301)
            if gearscore == 37:
                dungeon_score = random.randrange(216,301)
            if gearscore == 38:
                dungeon_score = random.randrange(221,301)
            if gearscore == 39:
                dungeon_score = random.randrange(226,301)
            if gearscore == 40:
                dungeon_score = random.randrange(231,301)
            if gearscore == 41:
                dungeon_score = random.randrange(236,301)
            if gearscore == 42:
                dungeon_score = random.randrange(241,301)
            if gearscore == 43:
                dungeon_score = random.randrange(246,301)
            if gearscore == 44:
                dungeon_score = random.randrange(251,301)
            if gearscore == 45:
                dungeon_score = random.randrange(256,301)
            if gearscore == 46:
                dungeon_score = random.randrange(261,301)
            if gearscore == 47:
                dungeon_score = random.randrange(266,301)
            if gearscore == 48:
                dungeon_score = random.randrange(271,301)
            if gearscore == 49:
                dungeon_score = random.randrange(276,301)
            if gearscore == 50:
                dungeon_score = random.randrange(281,301)
            if gearscore == 51:
                dungeon_score = random.randrange(286,301)
            if gearscore == 52:
                dungeon_score = random.randrange(291,301)
            if gearscore == 53:
                dungeon_score = random.randrange(296,301)
            if gearscore >= 54:
                dungeon_score = 300
            print("you finished floor 1 and got " + str(dungeon_score) + " score")
            if dungeon_score < 10:
                luck = random.randrange(1,3)
                if luck == 1:
                    e = e + 1
                else:
                    print("you didn't get a chest this run")
                    print("")
                    print("--------------------------------------------------------------------------")
            if dungeon_score >= 10 and dungeon_score <= 30:
                luck = random.randrange (1,101)
                if luck == 1:
                    r = r + 1
                if luck > 1 and luck < 70:
                    e = e +1
                else:
                    print("you didn't get a chest this run")
            if dungeon_score > 30 and dungeon_score <= 50:
                luck = random.randrange (1,101)
                if luck > 0 and luck <= 2:
                    r = r + 1
                if luck > 2 and luck <= 80:
                    e = e + 1
                else:
                    print("you didn't get a chest this run")
            if dungeon_score > 50 and dungeon_score <= 80:
                luck = random.randrange (1,101)
                if luck > 0 and luck <= 4:
                    r = r + 1
                if luck > 4 and luck <= 90:
                    e = e + 1
                else:
                    print("you didn't get a chest this run")
            if dungeon_score > 80 and dungeon_score <= 120:
                luck = random.randrange (1,101)
                if luck > 0 and luck <= 7:
                    r = r + 1
                else:
                    e = e + 1
            if dungeon_score > 120 and dungeon_score <= 150:
                luck = random.randrange (1,101)
                if luck > 0 and luck <= 1:
                    t = t + 1
                if luck > 1 and luck <= 11:
                    r = r + 1
                else:
                    e = e + 1
            if dungeon_score > 150 and dungeon_score <= 180:
                luck = random.randrange (1,101)
                if luck > 0 and luck <= 2:
                    t = t + 1
                if luck > 2 and luck <= 14:
                    r = r + 1
                else:
                    e = e + 1
            if dungeon_score > 180 and dungeon_score <= 210:
                luck = random.randrange (1,101)
                if luck > 0 and luck <= 4:
                    t = t + 1
                if luck > 4 and luck <= 20:
                    r = r + 1
                else:
                    e = e + 1  
            if dungeon_score > 210 and dungeon_score <= 240:
                luck = random.randrange (1,101)
                if luck > 0 and luck <= 1:
                    u = u + 1
                if luck > 1 and luck <= 9:
                    t = t + 1
                if luck > 9 and luck <= 31:
                    r = r + 1
                else:
                    e = e + 1
            if dungeon_score > 240 and dungeon_score <= 270:
                luck = random.randrange (1,101)
                if luck > 0 and luck <= 5:
                    u = u + 1
                if luck > 5 and luck <= 20:
                    t = t + 1
                if luck > 20 and luck <= 60:
                    r = r + 1
                else:
                    e = e + 1
            if dungeon_score > 270 and dungeon_score <= 285:
                luck = random.randrange (1,101)
                if luck > 0 and luck <= 10:
                    u = u + 1
                if luck > 10 and luck <= 35:
                    t = t + 1
                if luck > 35 and luck <= 75:
                    r = r + 1
                else:
                    e = e + 1
            if dungeon_score > 285 and dungeon_score <= 299:
                luck = random.randrange (1,101)
                if luck > 0 and luck <= 20:
                    u = u + 1
                if luck > 20 and luck <= 50:
                    t = t + 1
                if luck > 50 and luck <= 90:
                    r = r + 1
                else:
                    e = e + 1
            if dungeon_score == 300:
                luck = random.randrange (1,101)
                if luck > 0 and luck <= 50:
                    u = u + 1
                if luck > 50 and luck <= 75:
                    t = t + 1
                if luck > 75 and luck <= 99:
                    r = r + 1
                else:
                    e = e + 1
            
            if e == 1:
                print("you got a wood chest")
                print("do you want to open it? (free)")
                print("(1) yes")
                print("(2) no")
                player_input = (input())
                if player_input == "1":
                    slot_1 = random.randrange (1,201)
                    slot_2 = random.randrange (1,101)
                    print("")
                    print("wood chest")
                    print("---------------------------------------------------------------------------------")
                    if slot_1 > 0 and  slot_1 <= 70:
                        print("nothing")
                        print("")
                        print("---------------------------------------------------------------------------------")
                    if slot_1 > 70 and slot_1 <= 94:
                        print("simple dagger (12%)")
                        print("")
                        print("---------------------------------------------------------------------------------")
                        amount[0] = amount[0] + 1
                    if slot_1 > 94 and slot_1 <= 104:
                        print("cloth headwrap (5%)")
                        print("")
                        print("---------------------------------------------------------------------------------")
                        amount[1] = amount[1] + 1
                    if slot_1 > 104 and slot_1 <= 110:
                        print("cloth tunic (3%)")
                        print("")
                        print("---------------------------------------------------------------------------------")
                        amount[2] = amount[2] + 1
                    if slot_1 > 110 and slot_1 <= 118:
                        print("cloth pants (4%)")
                        print("")
                        print("---------------------------------------------------------------------------------")
                        amount[3] = amount[3] + 1
                    if slot_1 > 118 and slot_1 <= 128:
                        print("cloth shoes (5%)")
                        print("")
                        print("---------------------------------------------------------------------------------")
                        amount[4] = amount[4] + 1
                    if slot_1 > 128 and slot_1 <= 148:
                        amount = random.randrange(1,3)
                    if number == 1:
                        print("1 simple fragment (10%)")
                        print("")
                        print("---------------------------------------------------------------------------------")
                        simple_fragments = simple_fragments + 1
                    elif number == 2:
                        print("2 simple fragments (10%)")
                        print("")
                        print("---------------------------------------------------------------------------------")
                        simple_fragments = simple_fragments + 2
                    if slot_1 > 148 and slot_1 <= 164:
                        print("stone club (8%)")
                        print("")
                        print("---------------------------------------------------------------------------------")
                        amount[10] = amount[10] + 1
                    if slot_1 > 164 and slot_1 <= 170:
                        print("leather cap (3%)")
                        print("")
                        print("---------------------------------------------------------------------------------")
                        amount[5] = amount[5] + 1
                    if slot_1 > 170 and slot_1 <= 174:
                        print("leather_tunic (2%)")
                        print("")
                        print("---------------------------------------------------------------------------------")
                        amount[6] = amount[6] + 1
                    if slot_1 > 174 and slot_1 <= 178:
                        print("leather pants (2%)")
                        print("")
                        print("---------------------------------------------------------------------------------")
                        amount[7] = amount[7] + 1
                    if slot_1 > 178 and slot_1 <= 184:
                        print("leather boots (3%)")
                        print("")
                        print("---------------------------------------------------------------------------------")
                        amount[8] = amount[8] + 1
                    if slot_1 > 184 and slot_1 <= 189:
                        print("simple saber (2,5%)")
                        print("")
                        print("---------------------------------------------------------------------------------")
                        amount[11] = amount[11] + 1
                    if slot_1 > 189 and slot_1 <= 190:
                        print("dungeon upgrade (0,5%)")
                        print("haha this isn't even in the game")
                        print("")
                        print("---------------------------------------------------------------------------------")
                    if slot_1 > 190 and slot_1 <= 192:
                        print("undead helmet (1%)")
                        print("")
                        print("---------------------------------------------------------------------------------")
                        amount[9] = amount[9] + 1
                    if slot_1 > 192 and slot_1 <= 198:
                        print("simple shield (3%)")
                        print("")
                        print("---------------------------------------------------------------------------------")
                        amount[12] = amount[12] + 1
                    if slot_1 > 198 and slot_1 <= 200:
                        print("claw talisman (1%)")
                        print("")
                        print("---------------------------------------------------------------------------------")
                        amount[13] = amount[13] + 1
                    if slot_2 > 0 and slot_2 <= 50:
                        addcoins = random.randrange (50,151)
                        print(str(addcoins) + " coins (50%)")
                        print("")
                        print("---------------------------------------------------------------------------------")
                        coins = coins + addcoins
                    if slot_2 > 50 and slot_2 <= 95:
                        addsimple_essence = random.randrange (5,21)
                        print(str(addsimple_essence) + " simple essence (45%)")
                        print("")
                        print("---------------------------------------------------------------------------------")
                        simple_essence = simple_essence + addsimple_essence
                    if slot_2 > 95 and slot_2 <= 100:
                        addundead_essence = random.randrange (2,11)
                        print(str(addundead_essence) + " undead essence (5%)")
                        print("")
                        print("---------------------------------------------------------------------------------")
                        undead_essence = undead_essence + addundead_essence
            if r == 1:
                ("you got a stone chest")
                ("do you want to open it?")
                ("(1) yes")
                ("(2) no") 
                player_input == (input())
                if player_input == "1":
                    slot_1 = random.randrange (1,201)
                    slot_2 = random.randrange (1,101)
                    if slot_1 > 0 and slot_1 <= 48:
                        print("nothing")
                    if slot_1 > 48 and slot_1 <= 72:
                        print("simple dagger (12%)")
                        amount[0] = amount[0] + 1
                    if slot_1 > 0 and slot_1 <= 70:
                        print("")
                        cloth_headwrap =  cloth_headwrap + 1
                    if slot_1 > 0 and slot_1 <= 70:
                        print("")
                        cloth_tunic = cloth_tunic + 1
                    if slot_1 > 0 and slot_1 <= 70:
                        print("")
                        cloth_pants = cloth_pants + 1
                    if slot_1 > 0 and slot_1 <= 70:
                        print("")
                        cloth_shoes = cloth_shoes + 1
                    if slot_1 > 0 and slot_1 <= 70:
                        print("")
                    if slot_1 > 0 and slot_1 <= 70:
                        print("")
                    if slot_1 > 0 and slot_1 <= 70:
                        print("")
                    print("")
                    print("--------------------------------------------------------------------------------------------------")
                
            if t == 1:
                ("you got an iron chest")
                ("do you want to open it?")
                ("(1) yes")
                ("(2) no")
                player_input == (input())
                if player_input == "1":
                    slot_1 = random.randrange (1,201)
                    slot_2 = random.randrange (1,201)
                    slot_3 = random.randrange (1,101)
                    print("the developer is currently to lazy to develope this")
            if u == 1:
                ("you got a bronze chest")
                ("do you want to open it?")
                ("(1) yes")
                ("(2) no")
                player_input = (input())
                if player_input == "1":
                    slot_1 = random.randrange (1,201)
                    slot_2 = random.randrange (1,201)
                    slot_3 = random.randrange (1,101)
                    print("the developer is currently too lazy to develope this")
            e = 0
            t = 0
            r = 0
            u = 0
                    
        if player_input == "2":
            print("you entered floor 2")
            for n in range ( 1,11 ):
                print(n)
                time.sleep(1)
                dungeon_score = random.randrange(1,6)
            if gearscore == 1:
                dungeon_score = random.randrange(1,11)
            if gearscore == 2:
                dungeon_score = random.randrange(5,16)
            if gearscore == 3:
                dungeon_score = random.randrange(8,21)
            if gearscore == 4:
                dungeon_score = random.randrange(11,26)
            if gearscore == 5:
                dungeon_score = random.randrange(14,30)
            if gearscore == 6:
                dungeon_score = random.randrange(17,34)
            if gearscore == 7:
                dungeon_score = random.randrange(20,38)
            if gearscore == 8:
                dungeon_score = random.randrange(23,42)
            if gearscore == 9:
                dungeon_score = random.randrange(27,46)
            if gearscore == 10:
                dungeon_score = random.randrange(30,51)
            if gearscore == 11:
                dungeon_score = random.randrange(33,56)
            if gearscore == 12:
                dungeon_score = random.randrange(37,61)
            if gearscore == 13:
                dungeon_score = random.randrange(41,66)
            if gearscore == 14:
                dungeon_score = random.randrange(44,71)
            if gearscore == 15:
                dungeon_score = random.randrange(47,76)
            if gearscore == 16:
                dungeon_score = random.randrange(50,81)
            if gearscore == 17:
                dungeon_score = random.randrange(53,86)
            if gearscore == 18:
                dungeon_score = random.randrange(56,91)
            if gearscore == 19:
                dungeon_score = random.randrange(59,96)
            if gearscore == 20:
                dungeon_score = random.randrange(62,101)
            if gearscore == 21:
                dungeon_score = random.randrange(65,106)
            if gearscore == 22:
                dungeon_score = random.randrange(68,111)
            if gearscore == 23:
                dungeon_score = random.randrange(71,116)
            if gearscore == 24:
                dungeon_score = random.randrange(74,121)
            if gearscore == 25:
                dungeon_score = random.randrange(77,126)
            if gearscore == 26:
                dungeon_score = random.randrange(80,131)
            if gearscore == 27:
                dungeon_score = random.randrange(83,136)
            if gearscore == 28:
                dungeon_score = random.randrange(86,141)
            if gearscore == 29:
                dungeon_score = random.randrange(89,146)
            if gearscore == 30:
                dungeon_score = random.randrange(92,151)
            if gearscore == 31:
                dungeon_score = random.randrange(95,156)
            if gearscore == 32:
                dungeon_score = random.randrange(98,161)
            if gearscore == 33:
                dungeon_score = random.randrange(101,166)
            if gearscore == 34:
                dungeon_score = random.randrange(104,171)
            if gearscore == 35:
                dungeon_score = random.randrange(107,176)
            if gearscore == 36:
                dungeon_score = random.randrange(110,181)
            if gearscore == 37:
                dungeon_score = random.randrange(113,186)
            if gearscore == 38:
                dungeon_score = random.randrange(116,191)
            if gearscore == 39:
                dungeon_score = random.randrange(119,196)
            if gearscore == 40:
                dungeon_score = random.randrange(122,201)
            if gearscore == 41:
                dungeon_score = random.randrange(125,206)
            if gearscore == 42:
                dungeon_score = random.randrange(128,211)
            if gearscore == 43:
                dungeon_score = random.randrange(131,216)
            if gearscore == 44:
                dungeon_score = random.randrange(134,221)
            if gearscore == 45:
                dungeon_score = random.randrange(137,231)
            if gearscore == 46:
                dungeon_score = random.randrange(140,241)
            if gearscore == 47:
                dungeon_score = random.randrange(143,251)
            if gearscore == 48:
                dungeon_score = random.randrange(146,261)
            if gearscore == 49:
                dungeon_score = random.randrange(149,271)
            if gearscore == 50:
                dungeon_score = random.randrange(152,281)
            if gearscore == 51:
                dungeon_score = random.randrange(155,291)
            if gearscore == 52:
                dungeon_score = random.randrange(158,301)
            if gearscore == 53:
                dungeon_score = random.randrange(161,301)
            if gearscore == 54:
                dungeon_score = random.randrange(164,301)
            if gearscore == 55:
                dungeon_score = random.randrange(167,301)
            if gearscore == 56:
                dungeon_score = random.randrange(170,301)
            if gearscore == 57:
                dungeon_score = random.randrange(174,301)
            if gearscore == 58:
                dungeon_score = random.randrange(178,301)
            if gearscore == 59:
                dungeon_score = random.randrange(182,301)
            if gearscore == 60:
                dungeon_score = random.randrange(186,301)
            if gearscore == 61:
                dungeon_score = random.randrange(190,301)
            if gearscore == 62:
                dungeon_score = random.randrange(194,301)
            if gearscore == 63:
                dungeon_score = random.randrange(198,301)
            if gearscore == 64:
                dungeon_score = random.randrange(202,301)
            if gearscore == 65:
                dungeon_score = random.randrange(206,301)
            if gearscore == 66:
                dungeon_score = random.randrange(210,301)
            if gearscore == 67:
                dungeon_score = random.randrange(214,301)
            if gearscore == 68:
                dungeon_score = random.randrange(218,301)
            if gearscore == 69:
                dungeon_score = random.randrange(222,301)
            if gearscore == 70:
                dungeon_score = random.randrange(226,301)
            if gearscore == 71:
                dungeon_score = random.randrange(230,301)
            if gearscore == 72:
                dungeon_score = random.randrange(234,301)
            if gearscore == 73:
                dungeon_score = random.randrange(238,301)
            if gearscore == 74:
                dungeon_score = random.randrange(242,301)
            if gearscore == 75:
                dungeon_score = random.randrange(246,301)
            if gearscore == 76:
                dungeon_score = random.randrange(250,301)
            if gearscore == 77:
                dungeon_score = random.randrange(254,301)
            if gearscore == 78:
                dungeon_score = random.randrange(258,301)
            if gearscore == 79:
                dungeon_score = random.randrange(262,301)
            if gearscore == 80:
                dungeon_score = random.randrange(266,301)
            if gearscore == 81:
                dungeon_score = random.randrange(270,301)
            if gearscore == 82:
                dungeon_score = random.randrange(274,301)
            if gearscore == 83:
                dungeon_score = random.randrange(278,301)
            if gearscore == 84:
                dungeon_score = random.randrange(282,301)
            if gearscore == 85:
                dungeon_score = random.randrange(286,301)
            if gearscore == 86:
                dungeon_score = random.randrange(290,301)
            if gearscore == 87:
                dungeon_score = random.randrange(294,301)
            if gearscore == 88:
                dungeon_score = random.randrange(298,301)
            if gearscore >= 89:
                dungeon_score = 300
            print("you finished floor 2 and got " + str(dungeon_score) + " score")
            print("the developer is currently too lazy to develope this")
        if player_input == "3":
            print("you entered floor 3")
            for n in range ( 1,11 ):
                print(n)
                time.sleep(1)
            print("the developer currently is too lazy to develop this")
            print("")
            print("----------------------------------------------------------------------------------------------------------------")
        if player_input == "4":
            print("you entered floor 4")
            for n in range ( 1,11 ):
                print(n)
                time.sleep(1)
            print("the developer currently is too lazy to develop this")
            print("")
            print("----------------------------------------------------------------------------------------------------------------")   
        if player_input == "5":
            print("you entered floor 5")
            for n in range ( 1,11 ):
                print(n)
                time.sleep(1)
            print("the developer currently is too lazy to develop this")
            print("")
            print("----------------------------------------------------------------------------------------------------------------")
        if player_input == "6":
            print("you entered floor 6")
            for n in range ( 1,11 ):
                print(n)
                time.sleep(1)
            print("the developer currently is too lazy to develop this")
            print("")
            print("----------------------------------------------------------------------------------------------------------------")
        if player_input == "7":
            print("you entered floor 7")
            for n in range ( 1,11 ):
                print(n)
                time.sleep(1)
            print("the developer currently is too lazy to develop this")
            print("")
            print("----------------------------------------------------------------------------------------------------------------")


    elif player_input == "5":
        print("you currently have the following equip")
        for i in range (0,14):
            if amount[i] >= 0:
                print(gear[i] + ": " + "gearscore: " + str(score[i]))
        print("")
        
        print("what are you doing here?")
        time.sleep (1)
        print("what do you want to salvage huh?")
        time.sleep (2)
        print("seriously theres nothing here")
        time.sleep (3)
        print("go theres nothing to see here")
        time.sleep (5)
        print("why are you still here???????")
        time.sleep (10)
        print("ok, ok the code is hiddenwaffles")
        print("")

    elif player_input == "6":

        if z == 0:
            print("(1) simple strenght (+1 gearscore) 100 simple essence")
        if y == 0:
            print("(2) undead strenght (+2 gearscore) 50 undead essence")
        print("(3) extra chest 1 (gain extra chest from floor 1) 50 simple essence")
        if player_input == 1 and simple_essence >= 100 and z == 0:
            gearscore = gearscore + 1
            simple_essence = simple_essence - 100
            z = z + 1
            print("You feel empowered and gain 1 gearscore")
        elif player_input == 2 and undead_essence >= 100 and y == 0:
            gearscore = gearscore + 2
            undead_essence = undead_essence - 50
            y = y + 1
            print("A sense of invulnerability runs trough you, you gain 2 gearscore")
            
    elif player_input == "7":
        print("floor 1:")
        print("wooden chest (free):")
        print("slot 1:")
        print("nothing: 35%")
        print("simple dagger: 12%")
        print("cloth headwrap: 5%")
        print("cloth tunic: 3%")
        print("cloth pants: 4%")
        print("cloth shoes: 5%")
        print("simple fragment: 10% (1-2)")
        print("stone club: 8%")
        print("leather cap: 3%")
        print("leather tunic: 2%")
        print("leather pants: 2%")
        print("leather boots: 3%")
        print("simple saber: 2,5%")
        print("undead helmet: 1%")
        print("dungeon upgrade: 0.5%")
        print("simple shield: 3%")
        print("claw talisman: 1%")
        print("slot 2:")
        print("coins: 50% (30-120)")
        print("simple essence: 45% (5-20)")
        print("undead essence: 5% (2-10)")
        print("")
        print("stone chest (100 coins to unlock):")
        print("slot 1:")
        print("nothing : 24%")
        print("simple dagger: 12%")
        print("cloth headwrap: 5%")
        print("cloth tunic: 3%")
        print("cloth pants: 4%")
        print("cloth shoes: 5%")
        print("simple fragment: 12% (1-3")
        print("stone club: 10%")
        print("leather cap: 4%")
        print("leather tunic: 2,5%")
        print("leather pants: 3%")
        print("leather boots: 4%")
        print("simple saber: 3,5%")
        print("undead helmet: 1,5%")
        print("dungeon upgrade: 1%")
        print("simple shield: 4%")
        print("claw talisman: 1,5%")
        print("slot 2:")
        print("coins: 50% (50-200)")
        print("simple essence: 40% (7-30)")
        print("undead essence: 10% (3-15)")
        print("")
        print("iron chest (250 coins to unlock)")
        print("slot 1")
        print("nothing: 15%")
        print("simple dagger: 10%")
        print("floor 2:")
        print("floor 3:")
        print("floor 4:")
        print("floor 5:")
        print("floor 6:")
        print("floor 7:")
        print("")
        print("---------------------------------------------------------------------------")
    elif player_input == "8":
        x = x + 1
        print("your game was sucessfully exited")
        
    elif player_input == "9":   
        print("Tutorial:")
        print("Resources:")
        print("Your main resources in dungeons are gold, items and gearscore")
        print("Gold is used to open chests and upgrading equip both are important to gain more gearscore which allows you to play harder dungeons")
        print("items are used as equip or to upgrade equip and can also be sold or salvaged for other items")
        print("your main goal is to get as high as possible gearscore")
        print("dungeons:")
        print("dungeons are the origin of any kind of item in this game")
        print("depending on the difficulty and your current gearscore, you will get a score after you enter a dungeon, the maximum score is 300")
        print("depending on the score you got you will get a loot chest at the end of a dungeon which you can choose to open")
        print("some chests contain better items than others, you can view the loot tables in the main menu")
        print("opening chests costs gold so you better have some on your hands at all times, however there is also a free chest if you should ever run out")
        print("items:")
        print("every equip item gives you a certain amount of gearscore, however of some types of items you can only have 1 equipped at a time, this includes weapons and armor")
        print("of some items like talismans however you can equip every unique one you find on your journey")
        print("you can also upgrade items trough fragments and essences")
        print("fragments apply the fragmented effect, while essences apply stars")
        print("to fragment an item you need 8 of the respective fragments, the cost for stars varies")
        print("Good Luck on your journey trough the dungeons!")
        print("")
        print("--------------------------------------------------------------------------")
    
    elif player_input == "10":
        print("what are you here for?")
        time.sleep (1)
        print("you need a code")
        time.sleep (3)
        print("enter your code NOW!")
        player_input = (input())
        if player_input == "hiddenwaffles" and m == 0:
            print("you get 1000 coins!")
            coins = coins + 1000
            print("how did you .... ")
            print("I thought it was safe")
            print("that upgrade smith is in some trouble now")
            m = m + 1
        if m == 1:
            print("for the next thing I need you to think of the most painful thing you can imagine!")
            player_input = (input())
            if player_input == "juju" or "juju shortbow" or "Juju" or "Juju Shortbow" or "Jujuwette" or "Juju Wette" or "juju wette" or "die Wette" or "Die Wette" or "die wette":
                print("you get 1000 coins!")
                coins = coins + 1000
                print("how did you figure that out again????")
                time.sleep (2)
                print("seriously I don't have anymore codes for you")
                time.sleep (3)
                





