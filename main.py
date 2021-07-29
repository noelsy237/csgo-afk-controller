import time, sched, keyboard

scheduler = sched.scheduler(time.time, time.sleep)
logLocation = "D:\Games\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\consolelog.log"

gunList = {
    "ak": "ak47",
    "m4": "m4a4",
    "m4-s": "m4a1_silencer",
    "deagle": "deagle",
    "five7": "fiveseven",
    "mp9": "mp9",
    "p90": "p90",
    "ssg": "ssg08",
    "xm": "xm1014",
    "negev": "negev"
}

requestedDrops = []
requestedHelp = []

def getDropLine():
        lines = list(open(logLocation, "r", encoding='utf-8'))
        lastLines = lines[-10:]
        for line in lastLines:
            gun = line.partition("!drop")[2].strip()
            requester = line.partition("!drop")[0][:-2]
            if "!drop" in line and requester not in requestedDrops: 
                checkGun(gun, requester)
                break
            elif "!help" in line and requester not in requestedHelp:
                getHelp()
                requestedHelp.append(requester)

        print("File Checked")


def checkGun(gun, requester):   
    dropGun = None
    if gun in gunList:
        dropGun = gunList[gun]
    
    if dropGun:
        print(f"{gun} was requested by {requester}")
        keyboard.write(f"buy {dropGun}; drop")
        keyboard.press_and_release('enter')
        requestedDrops.append(requester)
    
    else:
        print("Invalid gun selection")
        keyboard.write(f"say Invalid gun selection. Try !help")
        keyboard.press('enter')


def getHelp():
    keyboard.write("say Usage: '!' followed by 'drop gun' (one per player); say Available guns to drop are:")
    keyboard.press('enter')
    gunString = ""
    for key in gunList:
        gunString += ", " + key
    keyboard.write(f"say {gunString}")
    keyboard.press('enter')


print("AFK Controller Initialised")
while True:
    e1 = scheduler.enter(1, 1, getDropLine)
    scheduler.run()