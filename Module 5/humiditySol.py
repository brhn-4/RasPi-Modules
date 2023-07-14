
########################################################################
# Filename    : humiditySol.py
# Description : Display air temp, water temp, and humidity on lcd
# Author      : brhn
# modification: 7/13/2024
########################################################################
from PCF8574 import PCF8574_GPIO
import Adafruit_DHT
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import sleep, strftime
from datetime import datetime
import os

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 21

def sensor(): #need array for the return serial numbers
    ret = []
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ret.append(i)
    return ret
def read(ds18b20): #multiple sensor serial nums
    data = []
    for sensor in ds18b20: #loop through each serial num
        location = '/sys/bus/w1/devices/' + sensor + '/w1_slave'  #data file
        tfile = open(location) #open
        text = tfile.read() # read
        tfile.close() # close
        secondline = text.split("\n")[1]  
        temperaturedata = secondline.split(" ")[9]
        temperature = float(temperaturedata[2:])
        celsius = temperature / 1000
        farenheit = (celsius * 1.8) + 32
        data.append(farenheit)
    return data


    
def loop(ds18b20):  

    mcp.output(3,1)     # turn on LCD backlight
    lcd.begin(16,2)     # set number of LCD lines and columns

    while(True):         
        lcd.clear()
        lcd.setCursor(0,0)  # set cursor position
        if read(ds18b20) != None:

            lcd.message ("A_Temp: %0.1f F" % read(ds18b20)[0] +'\n')     
            lcd.message ("W_Temp: %0.1f F" % read(ds18b20)[1] +'\n')  
        
        sleep(3)
        lcd.clear()

        humidity, jawn = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN) # set 'humidity' object
        if humidity is not None: #null check. Note: sometimes humidity will read null and skip therefore dispalying temps twice in a row.
            lcd.message("Humidity: {0:0.1f}%".format(humidity))
            
        sleep(3)

            
            
    
        
def destroy():
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
# Create LCD, passing in MCP GPIO adapter.
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)

if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        serialNums = sensor()
        loop(serialNums)
    except KeyboardInterrupt:
        destroy()

