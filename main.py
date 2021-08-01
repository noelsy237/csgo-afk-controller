import time, sched, keyboard

logLocation = "D:\Games\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\consolelog.log"

scheduler = sched.scheduler(time.time, time.sleep)
requestedDrops = []
requestedHelp = []
bombDropped = False
currentSeconds = 0
gunList = {
    "ak": "ak47",
    "m4": "m4a1",
    "m4-s": "m4a1_silencer",
    "deagle": "deagle",
    "p250": "p250",
    "five7": "fiveseven",
    "mp9": "mp9",
    "p90": "p90",
    "ssg": "ssg08",
    "xm": "xm1014",
    "negev": "negev"
}


def getDropLine():
    global currentSeconds
    if currentSeconds > 30:
        currentSeconds = 0
        resetRoundChecks()

    lines = list(open(logLocation, "r", encoding='utf-8'))
    lastLines = lines[-20:]
    for line in lastLines:
        gun = line.partition("!drop")[2].strip()
        player = line.partition("!drop")[0][:-2]
        if "!drop" in line and player not in requestedDrops: 
            checkGun(gun, player)
            break
        elif "!help" in line and player not in requestedHelp:
            getHelp()
            requestedHelp.append(player)
    currentSeconds += 1
    print("Checked for requests")


def checkGun(gun, player):   
    global bombDropped
    dropGun = None
    if gun in gunList:
        dropGun = gunList[gun]
    
    elif gun == "bomb" or "c4" and bombDropped is False:
        print(f"The bomb was dropped by {player}")
        bombDropped = True
        keyboard.write(f"use weapon_c4;drop")
        keyboard.press_and_release('enter')
    
    if dropGun:
        print(f"{gun} was requested by {player}")
        requestedDrops.append(player)
        keyboard.write(f"buy {dropGun};drop")
        keyboard.press_and_release('enter')


def getHelp():
    keyboard.write("say_team Usage: '!' followed by 'drop gun' (one per player); say_team Available guns to drop are:")
    keyboard.press('enter')
    gunString = ""
    for key in gunList:
        gunString += ", " + key
    keyboard.write(f"say_team {gunString}")
    keyboard.press('enter')


def resetRoundChecks():
    global bombDropped
    print("Round checks cleared")
    requestedDrops.clear()
    requestedHelp.clear()
    bombDropped = False
    

print("AFK Controller Initialised. Make sure to tab into the game and open the console.")
time.sleep(5)
keyboard.write(f"say_team AFK Controller Initialised. Try !help for additional information;+right")
keyboard.press('enter')
while True:
    e1 = scheduler.enter(1, 1, getDropLine)
    scheduler.run()