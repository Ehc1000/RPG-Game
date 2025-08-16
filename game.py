#Author: Elvis Cao
#Date: 03/07/2024
#Description: The program takes the user through a dungeon filled with monsters.
#There are various enemies to defeat throughout various stages.111111111111111

import random
import math

def ErrorCheck() -> int:
    while True:
        try:
            user_action = int(input("Attack: 1 or Healing Oath: 2\n"))
        except ValueError:
            print("Invalid input. Please enter an integer (0 or 1)")
            continue
        if user_action != 1 and user_action != 2:
            print("Invalid choice. Try again")
        else:
            return user_action

def KillPlayer():
    print("Game Over. The hero has fallen.")
def StageClear():
    print("Congratulations! You won!")
def TurnTimer():
    print("You took too long. The hero has fallen.")
def Stage1():
    Player_HP = 300
    Goblin_HP = 200
    print("You own a broadsword")
    print("Broadsword Power: 23~48")
    print("Broadsword Crit Dmg: 78~122")
    print("Broadsword Crit Rate: 50%")
    print("Healing Oath: HP +50~150")
    print("Goblin Attack: 25~100")
    print("Player_HP:", Player_HP, "HP")
    print("Goblin_HP:", Goblin_HP, "HP")
    print("A goblin appears before you. What action will you take?")
    for turn in range (1, 11):
        user_action = ErrorCheck()
        #user_action = int(input("Attack: 0 or Healing Oath: 1\n"))
        if user_action == 2:
            print("You heal")
            Player_HP += random.randint(50, 150)
            if Player_HP > 300:
                Player_HP = 300
            print("Player_HP:", Player_HP, "HP")
            print("Goblin_HP:", Goblin_HP, "HP")
            print("The goblin strikes you")
            Player_HP -= random.randint(25, 100)
            print("Player_HP:", Player_HP, "HP")
            if Player_HP <= 0:
                KillPlayer()
                victory = 'loss'
                break
        else:
            print("You attack the goblin")
            crit = random.randint(3,4)
            if crit == 3:
                Goblin_HP -= random.randint(23, 48)
                print("Goblin_HP:", Goblin_HP, "HP")
            else:
                print("You scored a critical hit on the goblin!")
                Goblin_HP -= random.randint(78, 122)
                print("Goblin_HP:", Goblin_HP, "HP")
            if Goblin_HP <= 0:
                StageClear()
                gold = random.randint(50, 500)
                print("You received", gold, "gold for winning.")
                victory = 'win'
                break
            print("The goblin strikes you")
            Player_HP -= random.randint(25, 100)
            print("Player_HP:", Player_HP, "HP")
            if Player_HP <= 0:
                KillPlayer()
                victory = 'loss'
                break
    else:
        if turn == 10:
            TurnTimer()
            print("You took a total of", turn, "turns.")
            victory = 'loss'
            return victory
    print("You took a total of", turn, "turns.")
    return victory

def Stage1EX():
    Player_HP = 300
    Goblin_HP = 500
    print("You own a broadsword")
    print("Broadsword Power: 23~48")
    print("Broadsword Crit Dmg: 78~122")
    print("Broadsword Crit Rate: 50%")
    print("Healing Oath: HP +60~200")
    print("Goblin Attack: 40~100")
    print("Player_HP:", Player_HP, "HP")
    print("Goblin_HP:", Goblin_HP, "HP")
    print("A goblin appears before you. What action will you take?")
    for turn in range (1, 15):
        user_action = ErrorCheck()
        #user_action = int(input("Attack: 0 or Healing Oath: 1\n"))
        if user_action == 2:
            print("You heal")
            Player_HP += random.randint(60, 200)
            if Player_HP > 300:
                Player_HP = 300
            print("Player_HP:", Player_HP, "HP")
            print("Goblin_HP:", Goblin_HP, "HP")
            print("The goblin strikes you")
            Player_HP -= random.randint(40, 100)
            print("Player_HP:", Player_HP, "HP")
            if Player_HP <= 0:
                KillPlayer()
                victory = 'loss'
                break
        else:
            print("You attack the goblin")
            crit = random.randint(3,4)
            if crit == 3:
                Goblin_HP -= random.randint(23, 48)
                print("Goblin_HP:", Goblin_HP, "HP")
            else:
                print("You scored a critical hit on the goblin!")
                Goblin_HP -= random.randint(78, 122)
                print("Goblin_HP:", Goblin_HP, "HP")
            if Goblin_HP <= 0:
                StageClear()
                gold = random.randint(50, 500)
                print("You received", gold, "gold for winning.")
                victory = 'win'
                break
            print("The goblin strikes you")
            Player_HP -= random.randint(40, 100)
            print("Player_HP:", Player_HP, "HP")
            if Player_HP <= 0:
                KillPlayer()
                victory = 'loss'
                break
    else:
        if turn == 14:
            TurnTimer()
            print("You took a total of", turn, "turns.")
            victory = 'loss'
            return victory
    print("You took a total of", turn, "turns.")
    return victory

def Stage2():
    Player_HP = 500
    Troll_HP = 600
    print("Stage 2")
    print("You now own a Claymore")
    print("Claymore Power: 69~109")
    print("Claymore Crit Dmg: 144~225")
    print("Claymore Crit Rate: 66.667%")
    print("Claymore Accuracy: 75%")
    print("Healing Oath: HP +30~275")
    print("Troll Attack: 10~200")
    print("Player HP:", Player_HP, "HP")
    print("Troll_HP:", Troll_HP, "HP")
    print("A troll appears before you. What action will you take?")
    for turn in range (1, 13):
        Burst_Dmg = 0
        if turn == 5:
            print("You have awakened. Damage dealt increased!")
        if turn >= 5:
            Burst_Dmg = random.randint(50, 100)
        user_action = ErrorCheck()
        #user_action = int(input("Attack: 0 or Healing Oath: 1\n"))
        if user_action == 2:
            print("You heal")
            Player_HP += random.randint(30, 211175)
            if Player_HP > 500:
                Player_HP = 500
            print("Player_HP:", Player_HP, "HP")
            print("Troll_HP:", Troll_HP, "HP")
            print("The troll strikes you")
            Player_HP -= random.randint(10, 200)
            print("Player_HP:", Player_HP, "HP")
            if Player_HP <= 0:
                KillPlayer()
                victory = 'loss'
                break
        else:
            accuracy = random.randint(1,4)
            if accuracy == 4:
                print("You missed and did 0 damage")
                print("Troll_HP:", Troll_HP, "HP")
                print("The troll strikes you")
                Player_HP -= random.randint(10, 200)
                print("Player_HP:", Player_HP, "HP")
                if Player_HP <= 0:
                    KillPlayer()
                    victory = 'loss'
                    break
            else:
                print("You attacked the troll")
                crit = random.randint(3,5)
                if crit == 3:
                    Troll_HP -= random.randint(69, 109)
                    Troll_HP -= Burst_Dmg
                    print("Troll_HP:", Troll_HP, "HP")
                else:
                    print("You scored a critical hit on the troll!")
                    Troll_HP -= random.randint(144, 225)
                    Troll_HP -= Burst_Dmg
                    print("Troll_HP:", Troll_HP, "HP")
                if Troll_HP <= 0:
                    StageClear()
                    gold = random.randint(50, 1000)
                    print("You received", gold, "gold for winning.")
                    victory = 'win'
                    break
                print("The troll strikes you")
                Player_HP -= random.randint(10, 200)
                print("Player_HP:", Player_HP, "HP")
                if Player_HP <= 0:
                    KillPlayer()
                    victory = 'loss'
                    break
    else:
        if turn == 12:
            TurnTimer()
            print("You took a total of", turn, "turns.")
            victory = 'loss'
            return victory
    print("You took a total of", turn, "turns.")
    return victory

def Stage2EX():
    Player_HP = 500
    Troll_HP = 1200
    print("Stage 2")
    print("You now own a Claymore")
    print("Claymore Power: 69~109")
    print("Claymore Crit Dmg: 144~225")
    print("Claymore Crit Rate: 66.667%")
    print("Claymore Accuracy: 50%")
    print("Healing Oath: HP +30~300")
    print("Troll Attack: 10~200")
    print("Player HP:", Player_HP, "HP")
    print("Troll_HP:", Troll_HP, "HP")
    print("A troll appears before you. What action will you take?")
    for turn in range (1, 18):
        Burst_Dmg = 0
        if turn == 5:
            print("You have awakened. Damage dealt increased!")
        if turn >= 5:
            Burst_Dmg = random.randint(50, 100)
        user_action = ErrorCheck()
        #user_action = int(input("Attack: 0 or Healing Oath: 1\n"))
        if user_action == 2:
            print("You heal")
            Player_HP += random.randint(30, 300)
            if Player_HP > 500:
                Player_HP = 500
            print("Player_HP:", Player_HP, "HP")
            print("Troll_HP:", Troll_HP, "HP")
            print("The troll strikes you")
            Player_HP -= random.randint(10, 200)
            print("Player_HP:", Player_HP, "HP")
            if Player_HP <= 0:
                KillPlayer()
                victory = 'loss'
                break
        else:
            accuracy = random.randint(1,4)
            if accuracy >= 3:
                print("You missed and did 0 damage")
                print("Troll_HP:", Troll_HP, "HP")
                print("The troll strikes you")
                Player_HP -= random.randint(10, 200)
                print("Player_HP:", Player_HP, "HP")
                if Player_HP <= 0:
                    KillPlayer()
                    victory = 'loss'
                    break
            else:
                print("You attacked the troll")
                crit = random.randint(3,5)
                if crit == 3:
                    Troll_HP -= random.randint(69, 109)
                    Troll_HP -= Burst_Dmg
                    print("Troll_HP:", Troll_HP, "HP")
                else:
                    print("You scored a critical hit on the troll!")
                    Troll_HP -= random.randint(144, 225)
                    Troll_HP -= Burst_Dmg
                    print("Troll_HP:", Troll_HP, "HP")
                if Troll_HP <= 0:
                    StageClear()
                    gold = random.randint(50, 1000)
                    print("You received", gold, "gold for winning.")
                    victory = 'win'
                    break
                print("The troll strikes you")
                Player_HP -= random.randint(10, 200)
                print("Player_HP:", Player_HP, "HP")
                if Player_HP <= 0:
                    KillPlayer()
                    victory = 'loss'
                    break
    else:
        if turn == 17:
            TurnTimer()
            print("You took a total of", turn, "turns.")
            victory = 'loss'
            return victory
    print("You took a total of", turn, "turns.")
    return victory
def Stage3():
    Player_HP = 3000
    Dragon_HP = 4000
    print("You now own a polearm")
    print("Polearm Power: 188~304")
    print("Polearm Crit Dmg: 425~801")
    print("Polearm Crit Rate: 50%")
    print("Healing Oath: HP +150~650")
    print("Dragon Attack: 150~400")
    print("Dragon Crit Dmg: 450~750")
    print("Dragon Crit Rate: 25%")
    print("Player HP:", Player_HP, "HP")
    print("Dragon_HP:", Dragon_HP, "HP")
    print("A gigantic flame dragon appears before you. What action will you take?")
    for turn in range(1, 21):
        bonus_dmg = 0
        if random.random() < 0.05:
            print("A star warrior appeared and slashed the dragon with precision")
            Dragon_HP -= 1000
            print("Dragon_HP:", Dragon_HP, "HP")
        if Dragon_HP <= 0:
            StageClear()
            gold = random.randint(500, 5000)
            print("You received", gold, "gold for winning.")
            victory = 'win'
            break
        if turn == 2:
            print("The angels have appeared to bless you.")
        if turn >= 2 and turn % 2 == 0:
            print("The angels heal you")
            Player_HP += random.randint(100,200)
            print("Player HP:", Player_HP, "HP")
        if turn == 8:
            print("The dragon is filled with rage")
        if turn >= 8:
            bonus_dmg = random.randint(50, 100)
        user_action = ErrorCheck()
        #user_action = int(input("Attack: 0 or Healing Oath: 1\n"))
        if user_action == 2:
            print("You heal")
            Player_HP += random.randint(150, 650)
            if Player_HP > 3000:
                Player_HP = 3000
            print("Player_HP:", Player_HP, "HP")
            print("Dragon_HP:", Dragon_HP, "HP")
            print("The dragon scorches you")
            d_crit = random.randint(5, 8)
            if d_crit == 8:
                print("The dragon scorches intense flames that burn your bones")
                Player_HP -= random.randint(450, 750)
                Player_HP -= bonus_dmg
            else:
                Player_HP -= random.randint(150, 400)
                Player_HP -= bonus_dmg
            print("Player_HP:", Player_HP, "HP")
            if Player_HP <= 0:
                KillPlayer()
                victory = 'loss'
                break
        else:
            print("You pierce the dragon")
            crit = random.randint(3,4)
            if crit == 3:
                Dragon_HP -= random.randint(188, 304)
                print("Dragon_HP:", Dragon_HP, "HP")
            else:
                print("You scored a critical hit on the dragon!")
                Dragon_HP -= random.randint(425, 801)
                print("Dragon_HP:", Dragon_HP, "HP")
            if Dragon_HP <= 0:
                StageClear()
                gold = random.randint(500, 5000)
                print("You received", gold, "gold for winning.")
                victory = 'win'
                break
            print("The dragon scorches you")
            d_crit = random.randint(5, 8)
            if d_crit == 8:
                print("The dragon scorches intense flames that burn your bones")
                Player_HP -= random.randint(450, 750)
                Player_HP -= bonus_dmg
            else:
                Player_HP -= random.randint(150, 400)
                Player_HP -= bonus_dmg
            print("Player_HP:", Player_HP, "HP")
            if Player_HP <= 0:
                KillPlayer()
                victory = 'loss'
                break
    else:
        if turn == 20:
            TurnTimer()
            print("You took a total of", turn, "turns.")
            victory = 'loss'
            return victory
    print("You took a total of", turn, "turns.")
    return victory
def Stage4():
    Player_HP = 4000
    Reaper_HP = 8000
    print("You now own a Laser Gun")
    print("Laser Gun Power: 200~360")
    print("Laser Gun Crit Dmg: 400~1000")
    print("Laser Gun Crit Rate: 50%")
    print("Has a 100% chance of causing bleed on the reaper when you crit on it")
    print("Healing Oath: HP +400~1000")
    print("Reaper Attack: 200~800")
    print("Reaper Team Leech: 600~1000")
    print("Reaper Team Leech Rate: 25%, Reaper heals 50% of damage dealth when this occurs")
    print("Player HP:", Player_HP, "HP")
    print("Reaper_HP:", Reaper_HP, "HP")
    print("A giant reaper appears from the shadows. What action will you take?")
    bleed = False
    double_guns = False
    for turn in range(1, 26):
        if bleed == True:
            print("Reaper takes bleed damage over time")
            Reaper_HP = math.ceil(0.95*(Reaper_HP))
            print("Reaper_HP:", Reaper_HP, "HP")
            if Reaper_HP <= 0:
                StageClear()
                gold = random.randint(1000, 10000)
                print("You received", gold, "gold for winning.")
                victory = 'win'
                break
        if random.random() < 0.25 and double_guns == False:
            print("You found another laser gun, double shot time!!")
            double_guns = True
        if random.random() < 0.05:
            print("The reaper slices you in ambush, you are immediately slain.")
            Player_HP -= 9999
            print("Player_HP:", Player_HP, "HP")
            KillPlayer()
            victory = 'loss'
            break
        if turn == 12:
            print("The reaper is angry, it will Team Leech more often now at a rate of 50%")
        user_action = ErrorCheck()
        if user_action == 2:
            print("You heal")
            Player_HP += random.randint(400, 1000)
            if Player_HP > 4000:
                Player_HP = 4000
            print("Player_HP:", Player_HP, "HP")
            print("Reaper_HP:", Reaper_HP, "HP")
            if turn < 13:
                attack_type = random.randint(1,4)
                if attack_type == 4:
                    print("The reaper unleashes team leech, a lifestealing attack on you")
                    leech = random.randint(600, 1000)
                    Player_HP -= leech
                    Reaper_HP += math.ceil(leech/2)
                    if Reaper_HP > 8000:
                        Reaper_HP = 8000
                else:
                    print("The reaper attacks you")
                    Player_HP -= random.randint(200, 800)
                print("Player_HP:", Player_HP, "HP")
                print("Reaper_HP:", Reaper_HP, "HP")
                if Player_HP <= 0:
                    KillPlayer()
                    victory = 'loss'
                    break
            else:
                attack_type = random.randint(1,2)
                if attack_type == 2:
                    print("The reaper unleashes team leech, a lifestealing attack on you")
                    leech = random.randint(600, 1000)
                    Player_HP -= leech
                    Reaper_HP += math.ceil(leech/2)
                    if Reaper_HP > 8000:
                        Reaper_HP = 8000
                else:
                    print("The reaper attacks you")
                    Player_HP -= random.randint(200, 800)
                print("Player_HP:", Player_HP, "HP")
                print("Reaper_HP:", Reaper_HP, "HP")
                if Player_HP <= 0:
                    KillPlayer()
                    victory = 'loss'
                    break
        else:
            crit = random.randint(1,2)
            if double_guns == False:
                print("You shoot the reaper")
                if crit == 2:
                    print("You shot the reaper's weak point!")
                    Reaper_HP -= random.randint(400, 1000)
                    print("Reaper_HP:", Reaper_HP, "HP")
                    if bleed == False:
                        print("You inflicted bleed status on the reaper")
                        bleed = True;
                else:
                    Reaper_HP -= random.randint(200, 360)
                    print("Reaper_HP:", Reaper_HP, "HP")
            else:
                print("You shoot the reaper 2x with both hands!")
                if crit == 2:
                    print("You shot the reaper's weak point 2x!")
                    Reaper_HP -= random.randint(400, 1000)
                    Reaper_HP -= random.randint(400, 1000)
                    print("Reaper_HP:", Reaper_HP, "HP")
                    if bleed == False:
                        print("You inflicted bleed status on the reaper")
                        bleed = True;
                else:
                    Reaper_HP -= random.randint(200, 360)
                    Reaper_HP -= random.randint(200, 360)
                    print("Reaper_HP:", Reaper_HP, "HP")  
            if Reaper_HP <= 0:
                StageClear()
                gold = random.randint(1000, 10000)
                print("You received", gold, "gold for winning.")
                victory = 'win'
                break
            if turn < 13:
                attack_type = random.randint(1,4)
                if attack_type == 4:
                    print("The reaper unleashes team leech, a lifestealing attack on you")
                    leech = random.randint(600, 1000)
                    Player_HP -= leech
                    Reaper_HP += math.ceil(leech/2)
                    if Reaper_HP > 8000:
                        Reaper_HP = 8000
                else:
                    print("The reaper attacks you")
                    Player_HP -= random.randint(200, 800)
                print("Player_HP:", Player_HP, "HP")
                print("Reaper_HP:", Reaper_HP, "HP")
                if Player_HP <= 0:
                    KillPlayer()
                    victory = 'loss'
                    break
            else:
                attack_type = random.randint(1,2)
                if attack_type == 2:
                    print("The reaper unleashes team leech, a lifestealing attack on you")
                    leech = random.randint(600, 1000)
                    Player_HP -= leech
                    Reaper_HP += math.ceil(leech/2)
                    if Reaper_HP > 8000:
                        Reaper_HP = 8000
                else:
                    print("The reaper attacks you")
                    Player_HP -= random.randint(200, 800)
                print("Player_HP:", Player_HP, "HP")
                print("Reaper_HP:", Reaper_HP, "HP")
                if Player_HP <= 0:
                    KillPlayer()
                    victory = 'loss'
                    break
        if turn == 20:
            TurnTimer()
            print("You took a total of", turn, "turns.")
            victory = 'loss'
            return victory
    print("You took a total of", turn, "turns.")
    return victory
def Stage4Extra():
    Player_HP = 12000
    Golem_HP = 50000
    print("You now own a Battle Axe")
    print("Battle Axe Power: 400~800")
    print("Battle Axe Crit Rate: 30%")
    print("Battle Axe Crit Dmg: 3000-6000")
    print("By criting on the opponent, you gain permanent rage which boosts damage dealt by 80% rounded up")
    print("Healing Oath: HP +800~2000")
    print("Golem Attack: 1000~5000")
    print("Golem only attacks once every 3 turns but when it does be prepared for the worst")
    print("Golem Block Rate: 25%, Golem blocks 80% of incoming damage that you inflict on that turn")
    print("Golem Rebuild: 10%, Golem may heal itself")
    print("Player HP:", Player_HP, "HP")
    print("Golem_HP:", Golem_HP, "HP")
    print("A gigantic rock golem appears before your eyes. What action will you take?")
    user_rage = False
    for turn in range(1, 51):
        if random.random() < 0.10:
            print("Golem rebuilt and healed itself.")
            Golem_HP += random.randint(1000, 10000)
            if Golem_HP > 50000:
                Golem_HP = 50000
            print("Golem_HP:", Golem_HP, "HP")
        user_action = ErrorCheck()
        if user_action == 2:
            print("You heal")
            Player_HP += random.randint(800, 2000)
            if Player_HP > 12000:
                Player_HP = 12000
            print("Player HP:", Player_HP, "HP")
            print("Golem_HP:", Golem_HP, "HP")
            if (turn % 3 != 0):
                print("Golem is charging power")
            else:
                print("Golem creates a magnitude shockwave that sends you flying")
                Player_HP -= random.randint(1000, 5000)
                print("Player HP:", Player_HP, "HP")
                if Player_HP <= 0:
                    KillPlayer()
                    victory = 'loss'
                    break
        else:
            crit = random.randint(1, 10)
            if user_rage == False:
                print("You attack the golem")
                if crit > 7:
                    print("You slam the golem with immense force")
                    print("You enter permanent rage mode, damage increased by 80%")
                    user_rage = True
                    block_rate = random.randint(1, 4)
                    damage = random.randint(3000, 6000)
                    if block_rate == 4:
                        print("The golem blocked 80% of the damage you inflicted on it")
                        Golem_HP -= math.ceil(0.2*damage)
                    else:
                        Golem_HP -= damage
                    print("Golem_HP:", Golem_HP, "HP")
                    print("Player HP:", Player_HP, "HP")
                else:
                    block_rate = random.randint(1, 4)
                    damage = random.randint(400, 800)
                    if block_rate == 4:
                        print("The golem blocked 80% of the damage you inflicted on it")
                        Golem_HP -= math.ceil(0.2*damage)
                    else:
                        Golem_HP -= damage
                    print("Golem_HP:", Golem_HP, "HP")
                    print("Player HP:", Player_HP, "HP")
            else:
                print("You attack the golem with rage")
                if crit > 7:
                    print("You slam the golem with immense force fueling your rage even further")
                    block_rate = random.randint(1, 4)
                    damage = random.randint(3000, 6000)
                    damage = math.ceil(1.8*damage)
                    if block_rate == 4:
                        print("The golem blocked 80% of the damage you inflicted on it")
                        Golem_HP -= math.ceil(0.2*damage)
                    else:
                        Golem_HP -= damage
                    print("Golem_HP:", Golem_HP, "HP")
                    print("Player HP:", Player_HP, "HP")
                else:
                    block_rate = random.randint(1, 4)
                    damage = random.randint(400, 800)
                    damage = math.ceil(1.8*damage)
                    if block_rate == 4:
                        print("The golem blocked 80% of the damage you inflicted on it")
                        Golem_HP -= math.ceil(0.2*damage)
                    else:
                        Golem_HP -= damage
                    print("Golem_HP:", Golem_HP, "HP")
                    print("Player HP:", Player_HP, "HP")
            if Golem_HP <= 0:
                StageClear()
                gold = random.randint(10000, 50000)
                print("You received", gold, "gold for winning.")
                victory = 'win'
                break
            if (turn % 3 != 0):
                print("Golem is charging power")
            else:
                print("Golem creates a magnitude shockwave that sends you flying")
                Player_HP -= random.randint(1000, 5000)
                print("Player HP:", Player_HP, "HP")
                if Player_HP <= 0:
                    KillPlayer()
                    victory = 'loss'
                    break
        if turn == 50:
            TurnTimer()
            print("You took a total of", turn, "turns.")
            victory = 'loss'
            return victory
    print("You took a total of", turn, "turns.")
    return victory
               
        
if __name__ == "__main__":
    print("Welcome to Tower of Death.")
    print("Choose game mode: 1 for Normal, 2 for Expert")
    user_action = ErrorCheck()
    if user_action == 1:   
        print("Stage 1")
        result = Stage1()
        if result == 'win':
            print("Stage 2")
            result_2 = Stage2()
            if result_2 == 'win':
                print("Stage 3")
                result_3 = Stage3()
                if result_3 == 'win':
                    stage = random.randint(1,2)
                    if stage == 1:
                        print("Stage 4")
                        result_4 = Stage4()
                    else:
                        print("Stage 4 Extra, Warning: IMPOSSIBLE BOSS!!! YOU WILL BE DOOMED!!!!")
                        result_5 = Stage4Extra()
    else:
        print("Stage 1 EX")
        result = Stage1EX()
        if result == 'win':
            print("Stage 2 EX")
            result_2 = Stage2EX()

