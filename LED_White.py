import time
import board
import neopixel
import RPi.GPIO as GPIO
pixels = neopixel.NeoPixel(board.D18, 30, brightness=1)
def turnWhiteRed(GL,BL):
    print("changing")
    loop = 0
    while loop<25:
        GL += 3
        BL += 10.2
        pixels.fill((GL,GL,BL))
        time.sleep(0.2)
        loop += 1

def turnWhiteBlue(GL,BL): 
    print("changing")
    loop = 0
    while loop<25:
        RL += 10.2
        GL += 10.2
        pixels.fill((GL,GL,BL))
        time.sleep(0.3)
        loop += 1