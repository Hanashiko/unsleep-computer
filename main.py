
import os
import platform
import time

try:
    import pyautogui  
except ImportError:
    os.system("pip install pyautogui")
    import pyautogui

def prevent_sleep():
    system = platform.system()

    if system == "Linux":
        os.system("caffeinate -d &")
        os.system("xset s off -dpms")  

    elif system == "Windows":
        os.system("powercfg -change -standby-timeout-ac 0")
        os.system("powercfg -change -monitor-timeout-ac 0")

    elif system == "Darwin":  # macOS
        os.system("caffeinate -d &")

    while True:
        pyautogui.press('shift')
        print("Комп'ютер не засне!")
        time.sleep(30)

if __name__ == "__main__":
    prevent_sleep()
