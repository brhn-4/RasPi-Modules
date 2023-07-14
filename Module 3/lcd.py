
########################################################################
# Filename    : lcd.py
# Description : Display Celsius and Farenheit Temperature from ds18b20 on LCD
# Author      : brhn
# modification: 7/13/2023
########################################################################

from PCF8574 import PCF8574_GPIO
import Adafruit_DHT
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import sleep, strftime
from datetime import datetime
import os

############################# INSTRUCTIONS #############################
# For this project you will need to complete 4 methods in order to 
# output the celsius and farenheit temperatures from the ds18b20
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
#         them to the lcd after. 
#
# 4. destroy()
#       - this method will clear the lcd and kill the program
#
# Note: you may need to change the pin numbers for the lcd object and
#       DHT_PIN
#
# SAMPLE OUTPUT:
#  Temp: 24.062 C
#  Temp: 75.312 F





DHT_SENSOR = Adafruit_DHT.DHT11
#DHT_PIN = 21


#Hint: use os.listdir()     
def sensor():

    return ds18b20
    
  
def read(ds18b20): 
    location = '/sys/bus/w1/devices/' + sensor + '/w1_slave'


    #celsius = 
    #farenheit = (celsius * 1.8) + 32
        
    return data
    
def loop(ds18b20):  

    mcp.output(3,1)     # LCD backlight
    lcd.begin(16,2)     # set number of lines and columns

    while(True):    #Output water temperature    
        #lcd.clear()
        lcd.setCursor(0,0)  # set cursor position
                           
        
def destroy(): #kill command, must clear lcd
    
    
PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
# Create PCF8574 GPIO adapter.
try:
    mcp = PCF8574_GPIO(PCF8574_address)
except:
    try:
        mcp = PCF8574_GPIO(PCF8574A_address)
    except:
        print ('I2C Address Error !')
        exit(1)

# Create lcd object and pass in MCP GPIO adapter. 
# lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp) 


if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        serialNums = sensor() #get serial number
        loop(serialNums)
    except KeyboardInterrupt: #kill
        destroy()

