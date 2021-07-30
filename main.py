import time, sched, keyboard

logLocation = "D:\Games\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\consolelog.log"

scheduler = sched.scheduler(time.time, time.sleep)
requestedDrops = []
requestedHelp = []
gunList = {
    "ak": "ak47",
    "m4": "m4a1",
    "m4-s": "m4a1_silencer",
    "deagle": "deagle",
    "five7": "fiveseven",
    "mp9": "mp9",
    "p90": "p90",
    "ssg": "ssg08",
    "xm": "xm1014",
    "negev": "negev"
}


def getDropLine():
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
        print("Checked for requests")


def checkGun(gun, player):   
    dropGun = None
    if gun in gunList:
        dropGun = gunList[gun]
    
    if dropGun:
        print(f"{gun} was requested by {player}")
        keyboard.write(f"buy {dropGun}; drop")
        keyboard.press_and_release('enter')
        requestedDrops.append(player)
    
    else:
        print("Invalid gun selection")
        keyboard.write(f"say_team Invalid gun selection. Try !help")
        keyboard.press('enter')


def getHelp():
    keyboard.write("say_team Usage: '!' followed by 'drop gun' (one per player); say_team Available guns to drop are:")
    keyboard.press('enter')
    gunString = ""
    for key in gunList:
        gunString += ", " + key
    keyboard.write(f"say_team {gunString}")
    keyboard.press('enter')


def resetPlayerArrays():
    requestedDrops.clear()
    requestedHelp.clear()


print("AFK Controller Initialised")
keyboard.write(f"say_team AFK Controller Initialised")
while True:
    e1 = scheduler.enter(1, 1, getDropLine)
    e2 = scheduler.enter(20, 1, resetPlayerArrays)
    scheduler.run()