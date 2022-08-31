from picographics import PicoGraphics, DISPLAY_TUFTY_2040

from random import seed
from random import random

import time

seed(1)

display = PicoGraphics(display=DISPLAY_TUFTY_2040)
WHITE = display.create_pen(255, 255, 255)

def getRandomByte():
    return int(random() * 255)

def getRandomFont():
    v = int(random() * 5)
    if v == 0:
        return "sans"
    elif v == 1:
        return "gothic"
    elif v == 2:
        return "cursive"
    elif v == 3:
        return "serif_italic"
    else:
        return "serif"

def setRandomPen():
    pen = display.create_pen(getRandomByte(), getRandomByte(), getRandomByte())
    display.set_pen(pen)

while(1):
    time.sleep(1)
    display.clear()
    
    #
    # Draw a random circle
    #
    
    r = int(random() * 100)
    x = int(random() * (320 - (2*r)))
    y = int(random() * 200)
    
    setRandomPen()
    display.circle(x, y, r)

    #
    # Draw random rectangle
    #
    
    w = int(random() * 200)
    h = int(random() * 200)
    x = int(random() * (320 - (w)))
    y = int(random() * 200)
    
    setRandomPen()
    display.rectangle(x, y, w, h)
    
    #
    # Draw text
    #
    
    text = "Hello Tufty"
    display.set_font(getRandomFont())
    
    s = int(random() * 3)
    width = display.measure_text(text, s, 1)
   
    x = int(random() * (320 - width))
    y = int(random() * 200)

    setRandomPen()

    display.text(text, x, y, 320, s)
    
    #
    # Trigger update
    #
    display.update()
    