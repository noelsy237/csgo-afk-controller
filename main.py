import pyautogui

logLocation = "D:\Games\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\console.log"

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

def getDropLine():
        lines = list(open(logLocation, "r", encoding='utf-8'))
        lastLines = lines[-20:]
        for line in lastLines:
            if "!drop" in line: 
                checkGun(line.partition("!drop")[2].strip(), line.partition("!drop")[0][:-2])
                break
            elif "!help" in line:
                getHelp()


def checkGun(gun, requester):   
    dropGun = None
    if gun in gunList:
        dropGun = gunList[gun]
    
    if dropGun:
        print(f"{gun} was requested by {requester}")
        pyautogui.write(f"buy {dropGun}")
        pyautogui.press('enter')
    
    else:
        print("Invalid gun selection")
        pyautogui.write(f"say Invalid gun selection. Try !help")
        pyautogui.press('enter')


def getHelp():
    pyautogui.write("say Usage: !drop gun")
    pyautogui.press('enter')
    pyautogui.write("say Available guns to drop are:")
    pyautogui.press('enter')
    gunString = ""
    for key in gunList:
        gunString += ", " + key
        
    pyautogui.write(f"say {gunString}")
    pyautogui.press('enter')

getDropLine()