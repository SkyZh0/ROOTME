from PIL import Image
import pytesseract
import pyautogui
import numpy as np
import pyautogui

SC = pyautogui.screenshot()

left = 80
top = 170
right = 330
bottom = 220

SC = SC.crop((left,top,right,bottom))

SC.convert("RGBA")
data = np.array(SC)

for x in data:
    for y in x:
        if y[0] == 0 and y[1] == 0 and y[2] == 0:
            y[0],y[1],y[2] = 255,255,255

for x in data:
    for y in x:
        if y[0] != 255 and y[1] != 255 and y[2] != 255:
            y[0],y[1],y[2] = 0,0,0

SC2 = Image.fromarray(data)

text = pytesseract.image_to_string(SC2)
pyautogui.moveTo(100, 250)
pyautogui.click()
pyautogui.typewrite(text)
pyautogui.press('enter')

print(text)
SC2.show()