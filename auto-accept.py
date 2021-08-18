import ctypes, pyautogui, time

user32 = ctypes.windll.user32

while True:
    pyautogui.click(user32.GetSystemMetrics(0)/2, user32.GetSystemMetrics(1)/2)
    time.sleep(5)