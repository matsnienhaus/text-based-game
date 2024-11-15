# when the original coder coded this only he and god knew what these lines of code did...
# now only god knows

import random
import time

# half of these variables aren't used anywhere but the repository owner forced me to keep them
z = 0
y = 0
secret = 0
coins = 500
gearscore = 0
simple_essence = 0
undead_essence = 0
simple_fragments = 0
dungeon_upgrade = 0
amount = 0
addsimple_essence = 0
addundead_essence = 0
dungeon_score = 0

gear = ["simple dagger", "cloth headwrap", "cloth tunic", "cloth pants", "cloth shoes", "leather cap", "leather tunic", "leather pants", "leather boots", "undead helmet", "stone club", "simple saber", "simple shield", "claw talisman"]
score = [5, 3, 5, 4, 3, 5, 7, 6, 4, 8, 7, 10, 5, 2]
price = [100, 40, 65, 50, 35, 70, 100, 85, 55, 150, 150, 220, 100, 120]
amount = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
equipped = [False, False, False, False, False, False, False, False, False, False, False, False, False, False,]
short = ["sd", "ch", "ct", "cp", "cs", "lc", "lt", "lp", "lb", "uh", "sc", "ss", "ssh", "cta"]


def enter_dungeon(floor):
    # i have a life so i wont add the dungeon system in this commit
    print("You've entered floor ", floor)
    difficulty = floor * 14



while True:
    print("you currently have the following items:")
    for i in range (0, len(gear)):
        if amount[i] > 0:
            print(gear[i] + ": " + str(amount[i]) + "x " + "gearscore: " + str(score[i]))
    print()
    print("you currently have these items equipped:")
    for i in range (0, len(gear)):
        if equipped[i] == True:
            print(gear[i] + ": " + "gearscore: " + str(score[i]))
    print()
            
    print("you currently have " + str(gearscore) + " gearscore")
    print("you currently have " + str(coins) + " coins")
    print()
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
    
    player_input = int(input())

    if player_input == 1:
        
        print("you currently have the following equip:")
        for i in range (0, len(gear)):
            if amount[i] > 0:
                print(gear[i] + ": " + str(amount[i]) + "x " + "gearscore: " + str(score[i]))
        print("")
            
        print("you have the following items equipped:")
        for i in range (0,len(gear)):
            if equipped[i] == True:
                print(gear[i] + ": " + "gearscore: " + str(score[i]))
        print("")
        
        print("what do you want to do?")
        print("(1) add equip")
        print("(2) remove equip")
        
        player_input = input()
        if player_input == "1":
            
            print("you have the following equip:")
            for i in range (0,len(gear)):
                if amount[i] > 0:
                    print(gear[i] + ": " + str(amount[i]) + "x " + "gearscore: " + str(score[i]) + "short: " + short[i])
                    
            print("which item do you want to equip?")
            player_input = input()
            index = short.index(player_input)
            if amount[index] > 0 and equipped[index] == False:
                amount[index] -= 1
                equipped[index] = True
                print("You have equipped: ", gear[index])
            else:
                print("You either don't have this item or you have it already equipped")
            print("")
            print("-----------------------------------------------------------------------------------------------")
                
                
        if player_input == "2":
            
            print("you have the following items equipped")
            for i in range (0,len(gear)):
                if equipped[i] == True:
                    print(gear[i] + ": " + "gearscore: " + str(score[i]) + " short: " + short[i])
            print("")
            print("which item do you want to unequip?")
            
            player_input = input()
            index = short.index(player_input)
            if equipped[index] == True:
                amount[index] += 1
                equipped[index] = False
                print("You have unequipped: ", gear[index])
            else:
                print("You don't have this item equipped")
            print("")
            print("----------------------------------------------------------------------------")
                       
    elif player_input == 2:
        print("what items do you want to sell?")
        print("you have the following items:")
        for i in range (0,len(gear)):
            if amount[i] > 0:
                print(gear[i] + ": " + str(amount[i]) + "x " + "price: " + str(price[i]) + " short: " + short[i])
        
        player_input = input()
        index = short.index(player_input)
        if amount[index] > 0:
            print("you have sold your " + gear[index] + " for " + str(price[index]) + " coins")
            amount[index] = amount[index] - 1
            coins += price[index]
            print("you now have " + str(coins) + " coins!")
        print("")
        print("-------------------------------------------------------------------------")
    
    elif player_input == 3:
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
    
    elif player_input == 4:
        print("which floor do you want to enter?")
        print("(1) floor 1 (recommended gearscore: 20)")
        print("(2) floor 2 (recommended gearscore: 40)")
        print("(3) floor 3 (recommended gearscore: 70)")
        print("(4) floor 4 (recommended gearscore: 120)")
        print("(5) floor 5 (recommended gearscore: 200)")
        print("(6) floor 6 (recommended gearscore: 350)")
        print("(7) floor 7 (recommended gearscore: 600)")
        print("Maximum score for all dungeons is 300!")
        player_input = int(input())
        enter_dungeon(player_input)

    elif player_input == 5:
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

    elif player_input == 6:

        if z == 0:
            print("(1) simple strength (+1 gearscore) 100 simple essence")
        if y == 0:
            print("(2) undead strength (+2 gearscore) 50 undead essence")
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
            
    elif player_input == 7:
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

    elif player_input == 8:
        print("Your game was sucessfully exited")
        break
        
    elif player_input == 9:   
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
    
    elif player_input == 10:
        if secret > 1:
            print("what are you here for?")
            time.sleep (1)
            print("you need a code")
            time.sleep (3)
            print("enter your code NOW!")
            player_input = (input())
            if player_input == "hiddenwaffles" and secret == 0:
                print("you get 1000 coins!")
                coins = coins + 1000
                print("how did you .... ")
                print("I thought it was safe")
                print("that upgrade smith is in some trouble now")
                secret += 1
            if secret == 1:
                print("for the next thing I need you to think of the most painful thing you can imagine!")
                player_input = input()
                if player_input.lower() == "juju" or "juju shortbow" or "jujuwette" or "juju wette" or "die wette":
                    print("you get 1000 coins!")
                    coins = coins + 1000
                    print("how did you figure that out again????")
                    time.sleep (2)
                    print("seriously I don't have anymore codes for you")
                    time.sleep (3)
        else: 
            print("seriously I don't have anymore codes for you")


