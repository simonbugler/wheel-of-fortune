import time                    
from time import sleep         
import apa  # RasPiO InsPiRing driver class

numleds = 24  # number of LEDs in our display
ledstrip = apa.Apa(numleds)    # initiate an LED strip

print ('Press Ctrl-C to quit.')

try:
    while True:
                     
        for led in range(numleds): # start single rotation loop

            ledstrip.led_set(led, 10, 0,0,255) # red pointer led
            ledstrip.led_set(led-12, 10, 255, 0, 0) # blue decoration led on opposite side B,G,R

            ledstrip.write_leds() # writes values to leds
            time.sleep(0.02) # framerate  or speed
            ledstrip.zero_leds() # zeros led values but does not write the values
        

finally:
    print("ALL LEDS OFF")
    ledstrip.reset_leds()