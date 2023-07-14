
########################################################################
# Filename    : waterTemp.py
# Description : Display Celsius and Farenheit Temperature from ds18b20
# Author      : brhn
# modification: 7/13/2023
########################################################################

import os

############################# INSTRUCTIONS #############################
# For this project you will need to complete 4 methods in order to 
# output the celsius and farenheit temperatures from the ds18b20 to the console
#
# 1. sensor()
#       -this method will read in the serial number of the sensor
#        and pass that serial number into read()
#
# 2. read()
#       - this method will take in the serial number, then
#         read in the w1_slave file and convert the raw data
#         into celsius and farenheit values
#
# 3. loop()
#       - this method will take in the temp values and output
#         them to the console after. 
#
# 4. destroy()
#       - this method will clear the lcd and kill the program
#
# Note: you may need to change the pin numbers for the lcd object and
#       DHT_PIN
#
# SAMPLE OUTPUT:
#  Current Temperature: 24.062 C
#  Current Temperature: 75.312 F
def sensor(): 
    
    return ds18b20

def read(ds18b20): 
   
    return celsius, farenheit

def loop(ds18b20):
    while True:
       

def kill(): #kill command


if __name__ == '__main__':
    try:
        serialNum = sensor()
        loop(serialNum)
    except KeyboardInterrupt:
        kill()
