import time                    
from time import sleep         
import apa  # RasPiO InsPiRing driver class
import random

numleds = 24  # number of LEDs in our display
ledstrip = apa.Apa(numleds)    # initiate an LED strip
spin = 0 # define spin number

winningnumbers = [6,12,18,24]
losingnumbers = [1,2,3,4,5,7,8,9,10,11,13,14,15,16,17,19,20,21,22,23]

print ('Press Ctrl-C to quit.')

def selectwinner(spin): # function for choosing winner

    winningspin = random.randint(3, 7) # randomisation of average winning spin

    if spin % winningspin == 0:
        numleds = random.sample(winningnumbers,  1)
        numleds = numleds[0]
    else:
        numleds = random.sample(losingnumbers,  1)
        numleds = numleds[0]


    winner = {
        "number":numleds, 
    }
    return winner

try:
    while True:

        numleds = 24 # reset to 24 after stopping at chosen

        rotations = 5

        spin += 1 # spin number going up by 1 each loop

        for rotation in range(rotations): # rotations in one spin

            if rotation == rotations - 1: # on last rotation of the spin stop at chosen led

                winner = selectwinner(spin)
                numleds = winner.get("number") # chosen winning or loser number
                     
            for led in range(numleds): # start single rotation loop

                ledstrip.led_set(led, 10, 0,0,255) # red pointer led
                ledstrip.led_set(led-12, 10, 255, 0, 0) # blue decoration led on opposite side B,G,R

                ledstrip.write_leds() # writes values to leds
                time.sleep(0.02) # framerate  or speed
                ledstrip.zero_leds() # zeros led values but does not write the values
            
        time.sleep(1.0)
        

finally:
    print("ALL LEDS OFF")
    ledstrip.reset_leds()