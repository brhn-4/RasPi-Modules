########################################################################
# Filename    : app.py
# Description : sensor fetch function. pass in data to DOM in index.html
# Author      : brhn
# modification: 8/19/2023
########################################################################




from flask import Flask, jsonify
from flask_cors import CORS
import Adafruit_DHT
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import sleep, strftime
from datetime import datetime
import os

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 21

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

def sensor(): #need array for the return serial numbers
    ret = []
    for i in os.listdir('/sys/bus/w1/devices'): #loop through dir
        if i != 'w1_bus_master1': #if != 'w1_bus_master1' then i == serialNum. used in read()
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

@app.route('/get_data', methods=['GET']) #get route
def get_data(): #get fcn
    ds18b20 = sensor() #call sensor fcn from earlier module to read in water and air temps
    temperatures = read(ds18b20)
    humidity, _ = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN) #call sensor fcn from earlier module to read in humidity

    return jsonify({ #return json obj
        'air_temperature':'%0.2f F' % temperatures[0],
        'water_temperature': '%0.2f F' % temperatures[1],
        'humidity': '%0.2f ' % humidity + '%'
    })

if __name__ == '__main__': #set host and port (0.0.0.0 allows multiple viewers)
    app.run(host='0.0.0.0',port=5000)
