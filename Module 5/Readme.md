
# Project 5: Humidity
Due: _________ at 11:59 PM <br>
Points: __________


## Introduction
For this project, we are going to be connecting a DHT11 Humidity Sensor to our raspberry pi.
<br><br>
This project will be split into two parts wiring the sensor to your Pi and then writing a Python script to read the input. Depending on the state of your Pi's repository you may need to update certain packages. If you run into any unexpected issues make sure to double check everything is up to date and that you have installed the new packages correctly.
<br><br>
**HARDWARE REQUIREMENTS**: 1x dht11 humidity sensor, Jumper wires, 10K Ohm Resistor (only for four pin module)

<br><br>
## DHT11
For this project we will be using the DHT11 humidity sensor. There are two variants of the DHT11 that are commonly used. One is a three pin PCB mounted module and the other is a four pin stand-alone module. During this project we will be working with the 3 pin module with a breakout board include however, the pinout is different for each one, so if you have the 4 pin variant make sure to look online for the correct wiring.
<p align="center">
  <img src="https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/de5f19de-5628-4e87-bfa1-9a4e7d7cedee" width="450" />
</p>




## Connecting the Sensor

- **Step 1**: First, like always you want to disconnect the power supply from your pi.
- **Step 2**: You can plug the dht11 directly into part of the unpowered breadboard or an auxiliray board.  
- **Step 3**: Connect the GND (black) pin to the GND GPIO pin of your Pi
- **Step 4**: Connect the VCC (red) pin to the 5v GPIO of your Pi
- **Step 5**: Connect the Signal (blue) pin to any generic GPIO of your Pi
- **Step 6**: Now that everything is connected we can power on our pi and begin coding!

  NOTE: Refer to the diagram below for clarification.


<p align="center">
  <img src="https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/c42eaaaa-4ab4-4239-a1c6-69ce54dbcc29" width="300" />
</p>


## Software Configuration

For this project we will be using the Adafruit Python library to help streamline our python script. The library is already included within the starter code files but if you would like to update it you can download the updated library using git. Now to finish installing the proper packages run the following commands
`````````
 cd Adafruit_Python_DHT
 sudo apt-get install build-essential python-dev
 sudo python setup.py install
`````````

## Python Script
For the Project 5 script, you will need to read in the humidity from your DHT11 sensor and output it to your LCD. We will be combining the work done in module 4 so that our LCD rotates between displaying water and air temperature to humidity every 3 seconds. Refer to the starter code for more details.
























