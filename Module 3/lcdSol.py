
########################################################################
# Filename    : lcdSol.py
# Description : Display Celsius and Farenheit Temperature from ds18b20 on LCD
# Author      : brhn
# modification: 7/13/2023
########################################################################

from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import sleep, strftime
from datetime import datetime
import os


#   Author note: please note that the sensor and read method are constructed to be able to handle multiple sensors which will be implemented later. Hence, they do some 
#                unnecessary work. The sensor method loops through the directory and appends every sensor serial number and returns it in ret. For this module however,
#                it is unnecessary. Additionally, read has a loop that loops through each sensor returned by read. This solution is hard coded in it's output to only return 
#                the water temperature. The student's solution will not need these loops and should simply read the serial number from sensor() and convert the raw data in read()

def sensor():
    ret = [] #for multiple sensors
    for i in os.listdir('/sys/bus/w1/devices'): #directory with w1
        if i != 'w1_bus_master1': #need to edit if have other i2c sensors in this directory
            ret.append(i)
    return ret

def read(ds18b20):
    data = []
    for sensor in ds18b20: #loop for multiple sensors in my devices directory
        location = '/sys/bus/w1/devices/' + sensor + '/w1_slave'
        tfile = open(location)
        text = tfile.read()
        tfile.close()
        secondline = text.split("\n")[1]
        temperaturedata = secondline.split(" ")[9]
        temperature = float(temperaturedata[2:])
        celsius = temperature / 1000
        farenheit = (celsius * 1.8) + 32
        data.append(celsius)
        data.append(farenheit)
    print(data)
    return data
    
def loop(ds18b20):  ###### HARD CODED FOR ONE SENSOR: WATER TEMP #######

    mcp.output(3,1)     # lcd backlight
    lcd.begin(16,2)     # set number of lines and columns

    while(True):         
        #lcd.clear()
        lcd.setCursor(0,0)  # set cursor position

        if read(ds18b20) != None: #null check
            lcd.message ("Temp: %0.3f C" % read(ds18b20)[2] +'\n') 
            lcd.message ("Temp: %0.3f F" % read(ds18b20)[3] +'\n') 

          
            
       
        
def destroy(): #kill command
    lcd.clear()
    quit()
    
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
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp) 

if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        serialNums = sensor() #get serial number
        loop(serialNums)
    except KeyboardInterrupt: #kill
        destroy()

