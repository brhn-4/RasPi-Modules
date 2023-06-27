
########################################################################
# Filename    : Blink.py
# Description : Basic GPIO Input, Led On/Off
# Author      : brhn
# modification: 6/27/2023
########################################################################
from gpiozero import LED
from time import sleep

# INSTRUCTIONS:
# For this assignment you will need to complete 3 different tasks.
# 1. Assign 'led' to the correct GPIO pin to be able to control the power output and turn on/off the LED

# 2. In the method 'blink()' you will need to create an infinitely running loop that will do the following:
#     - run until KeyboardInterrupt (you will need to complete the method 'destroy()' for this)
#     - turn the led on  -> sleep for 1 second -> turn led off -> sleep for 1 second
#     - Additionally after each on/off print a message to the terminal notfiying user if the LED is on or off
# 3. In the medthod 'fiveLongBlink()' you will need to do the following:
#     - create a loop that turns the led on for 4 seconds then turns off for 1 second
#     - this loop will run 5 times and then destroy()
#
# note: We have provided you with a main function that will be called upon execution. You will need to uncomment the method calls in the try block to test your methods

  
led =       # define LED pin according to BCM Numbering

def blink(): #infinit blink until keyboard interryp
   

def fiveLongBlink(): #5 long blinks
   

    
def destroy():
   


if __name__ == '__main__':  ##Called on execution
    print ('Program is starting ... ')
    try:     #Try calling main function 'blink'
        #blink()
        #fiveLongBlink()
    except KeyboardInterrupt:  #kill script
        destroy()
