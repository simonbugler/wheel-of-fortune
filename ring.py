import time                    
from time import sleep         
from datetime import datetime
import random
import apa  # RasPiO InsPiRing driver class
numleds = 24  # number of LEDs in our display
ledstrip = apa.Apa(numleds)    # initiate an LED strip

minrotations = 6
maxrotations = 24

brightness = 10  # 0-31, 224-255 or 0xE0-0xFF

winningnumbers = [6,12,18,24]
losingnumbers = [1,2,3,4,5,7,8,9,10,11,13,14,15,16,17,19,20,21,22,23]

spin = 0 # spin number
winning_spins = 0 # for testing average wins printed to console

def selectwinner(spins): # function for choosing winner

    global winning_spins # for testing average wins printed to console

    winningspin = random.randint(3, 7) # randomisation of average winning spin

    if spin % winningspin == 0:
        numleds = random.sample(winningnumbers,  1)
        numleds = numleds[0]
        led_colour = [0,255,0] # winning colour B,G,R
        winning_spins += 1 # for testing average wins printed to console
    else:
        numleds = random.sample(losingnumbers,  1)
        numleds = numleds[0]
        led_colour = [0,0,255] # losing colour B,G,R


    winner = {
        "numleds":numleds, 
        "led_colour":led_colour, 
        "winning_spins":winning_spins # for testing average wins printed to console
    }
    return winner

ledstrip.flush_leds()

print ('Press Ctrl-C to quit.')

try:
    while True:
        
        rotations = random.randint(minrotations, maxrotations) # randomised number of rotations in this spin
        
        numleds = 24 # reset to total number of leds after changing to chosen winner or loser

        decay = rotations * numleds # total number of leds in this spin - although more as last rotation is less

        spin += 1 # spin number going up each loop

        for rotation in range(1,rotations): # start spin - multiple rotations loop
            
            led_colour = [255,255,255] # default led colour B,G,R
            led_stop_colour  = [255,255,255] # reset to default colour B,G,R
            
            if rotation == rotations - 1: # on last rotation of spin select winning number

                winner = selectwinner(spin)
                led_stop_colour = winner.get("led_colour") # colour of winner or loser
                numleds = winner.get("numleds") # chosen winning or loser number
                winning_spins = winner.get("winning_spins") # for testing average wins printed to console

                # print("LED " + str(numleds)) # for testing print chosen led to console
                # print("Spin " + str(spin)) # for testing printed to console
                # print("Winning Spins " + str(winning_spins)) # for testing average wins printed to console

                
            for led in range(numleds): # start single rotation loop

                if led+1 == numleds: # if the last selected led - winner or loser
                    led_colour = led_stop_colour # changes colour based on winner or loser

                ledstrip.led_set(led, brightness, led_colour[0], led_colour[1], led_colour[2]) # pointer led

                ledstrip.led_set(led-15, brightness, 255, 0, 0)
                ledstrip.led_set(led-14, brightness, 128, 0, 0)
                ledstrip.led_set(led-13, brightness, 64, 0, 0)
                ledstrip.led_set(led-12, brightness, 32, 0, 0) # decoration leds on opposite side B,G,R
                ledstrip.led_set(led-11, brightness, 64, 0, 0)
                ledstrip.led_set(led-10, brightness, 128, 0, 0)
                ledstrip.led_set(led-9, brightness, 255, 0, 0)

                time.sleep(rotation/decay) # creates log style increasing time delay
                decay -= 1 # increases time delay per led

                ledstrip.write_leds()
                ledstrip.zero_leds()
        
        time.sleep(5.0) # infinite loop pause between spins

finally:
    print("ALL LEDS OFF")
    ledstrip.reset_leds()