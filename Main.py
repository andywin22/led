import time
import board
import neopixel
import RPi.GPIO as GPIO
import LED_Blue
import LED_Red
import LED_White

GPIO.setwarnings(False)
def gpioset():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #on off default colour
    GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #warm colour
    GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #cold colour

def buttondown():
    GPIO.add_event_detect(14,GPIO.FALLING,callback=lightfunc, bouncetime=1200) #IO 14 燈開關
    GPIO.add_event_detect(17,GPIO.FALLING,callback=lightwarm, bouncetime=1200) #IO 17 燈暖色
    GPIO.add_event_detect(24,GPIO.FALLING,callback=lightcold, bouncetime=1200) #IO 24 燈冷色
    
def lightfunc(channel):
    pixels = neopixel.NeoPixel(board.D18, 30, brightness=1)
    on_off +=1
    if on_off == 1:          #開燈
        print("light on")
        pixels.fill((255, 255,255))
        RL = 255
        GL = 255
        BL = 255
        ledMode = 1
        
    if on_off > 1 and ledMode == 1:   #關燈
        print("light off")
        pixels.fill((0, 0, 0))
        on_off = 0
        ledMode = 0
    
    if on_off > 1 and ledMode != 1:
        if(RL == 255 and GL == 150 and BL == 0):
           LED_White.turnWhiteRed(GL,BL)
        
        else:
            LED_White.turnWhiteBlue(GL,BL) 
        
        ledMode = 1 #結束後的紀錄
        RL = 255
        GL = 255
        BL = 255
            
def lightwarm(channel): #255 150 0   
    if ledMode == 1: #白燈
        LED_Red.turnRedWhite(GL,BL)
        
    if ledMode == 3: #冷燈
        LED_Red.turnRedBlue(RL,GL,BL)
    RL = 255
    GL = 150
    BL = 0
    ledMode = 2
    print("warm colour done")
    
def lightcold(channel): #0 0 255   
    if ledMode == 1: #白燈
        LED_Blue.turnBlueWhite(GL,BL)
        
    if ledMode == 2: #暖燈
        LED_Blue.turnBlueRed(GL,BL)
    RL = 0
    GL = 0
    BL = 255
    ledMode = 3
    print("cold colour done")
    return None
    
def main():
    pixels = neopixel.NeoPixel(board.D18, 30, brightness=1)
    pixels.fill((0,0,0))
    global on_off
    global ledMode
    global RL
    global GL
    global BL
    ledMode = 0     # defalut 1 warm 2 cold 3
    on_off = 0
    RL = 0
    GL = 0
    BL = 0
    gpioset()
    while True:
        buttondown()

main()
