import pyautogui, sys
import random
import time



list1 = [1, 2, 3, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400,]
list2 = [1 ,2, 3, 100, 200, 300, 400, 500, 600, 700, 800, 850]
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        pyautogui.moveTo(random.choice(list1), random.choice(list2), 1)
        pyautogui.dragTo(random.choice(list1), random.choice(list2), 1, button='left') 
        pyautogui.click()
        pyautogui.click(button='right') 
        time.sleep(2)
except KeyboardInterrupt:
    print('\n')

