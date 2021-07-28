import shutil
import os

#Config
#con_logfile "consolelog.log"

#pyautogui.write('Hello There')
logLocation = "D:\Games\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\consolelog.log"

def getDropLine():
        datafile = open(logLocation, encoding='utf-8')
        for line in datafile:
            if "!drop" in line:
                checkGun(line)
                break

def checkGun(line):
    print(line)

getDropLine()

    