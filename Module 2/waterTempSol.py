
########################################################################
# Filename    : waterTempSol.py
# Description : Display Celsius and Farenheit Temperature from ds18b20
# Author      : brhn
# modification: 7/13/2023
########################################################################

import os

def sensor(): #read in serialnums from os
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i
    return ds18b20

def read(ds18b20): #open raw file, convert into readable values
    location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    farenheit = (celsius * 1.8) + 32
    return celsius, farenheit

def loop(ds18b20): #output to console
    while True:
        if read(ds18b20) != None:
            print ("Current temperature : %0.3f C" % read(ds18b20)[0])
            print ("Current temperature : %0.3f F" % read(ds18b20)[1])

def kill(): #kill command
    quit()

if __name__ == '__main__':
    try:
        serialNum = sensor()
        loop(serialNum)
    except KeyboardInterrupt:
        kill()
