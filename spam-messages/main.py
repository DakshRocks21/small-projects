import pyautogui
import time

def spammy():
        pyautogui.FAILSAFE = False
        number = 1
        while True:
                time.sleep(0.1)
                pyautogui.write("Message #" + str(number))
                pyautogui.hotkey('enter')
                if (number % 50) == 0:
                        t = time.localtime()
                        current_time = time.strftime("%H:%M:%S", t)
                        print("Current Number is " + str(number) + " at " + str(current_time))
                number = number + 1

                if number > 10000:
                        exit()
