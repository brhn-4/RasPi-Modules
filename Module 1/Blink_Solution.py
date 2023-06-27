
########################################################################
# Filename    : Blink_Solution.py
# Description : Basic GPIO Input, Led On/Off
# Author      : brhn
# modification: 6/26/2023
########################################################################
from gpiozero import LED
from time import sleep



  
led = LED("GPIO5")       # define LED pin according to BCM Numbering

def blink():
    while True:
        led.on()    # turn on LED
        print ('led turned on')  # print message on terminal
        sleep(1)    # wait 1 second
        led.off()   # turn off LED 
        print ('led turned off')
        sleep(1)    # wait 1 second

def fiveLongBlink(): #5 long blinks
    for i in range(5):
        led.on() #turn on LED
        sleep(4) #sleep 4 seconds
        led.off() #turn off LED
        sleep(1) #sleep 1 second
    destroy()

    
def destroy():
    quit()


if __name__ == '__main__':  ##Called on execution
    print ('Program is starting ... ')
    try:     #Try calling main function 'blink'
        #blink()
        #fiveLongBlink()
    except KeyboardInterrupt:  #kill script
        destroy()
