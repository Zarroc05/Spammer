import random
import time

import keyboard
import pyautogui
from alive_progress import alive_bar


########################################################################################################################
def main():
    spamText = []
    flag = 'y'
    while flag == 'y':
        text = input("Spam Text : ")
        spamText.append(text)
        flag = input("Do you want to add more messages(y/n) : ")
        if flag == 'n':
            break
    count = int(input("How many times : "))
    interval = float(input("Time interval(sec) : "))
    sec = 5
    while not (sec < 0):
        timer = sec
        print("Spamming in ", timer, end="\r")
        time.sleep(1)
        sec -= 1
    with alive_bar(count, title="Spamming!", spinner="classic") as bar:
        for _ in range(count):
            pyautogui.typewrite(random.choice(spamText))
            pyautogui.press('enter')
            time.sleep(interval)
            print()
            bar()
    print('\nDone')
    print("Press any key to continue")
    keyboard.read_key()
########################################################################################################################
