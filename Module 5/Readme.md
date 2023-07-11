
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
  <img src="https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/de5f19de-5628-4e87-bfa1-9a4e7d7cedee" width="350" />
</p>




## Connecting the Sensor

Now when we are connecting the sensor we will have to re-wire our water temperature to create one circuit with both of the sensors that we connect to the Pi. 


- **Step 1**: First, like always you want to disconnect the power supply from your pi.
- **Step 2**: You can plug the dht11 directly into part of the unpowered breadboard or an auxiliray board.  
- **Step 3**: Connect the GND (black) pin to the GND GPIO pin of your Pi
- **Step 4**: Connect the VCC (red) pin to the 5v GPIO of your Pi
- **Step 5**: Connect the Signal (blue) pin to any generic GPIO of your Pi
- **Step 6**: Now that everything is connected we can power on our pi and begin coding!

  NOTE: Refere to the diagram below for clarification.


<p align="center">
  <img src="https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/c42eaaaa-4ab4-4239-a1c6-69ce54dbcc29" width="300" />
</p>


## Software Configuration

We’ll need to enable the One-Wire interface before the Pi can receive data from our sensor if you didn't already in module 2. Once you have the sensor fully connected, the pi powered on, and you are logged in follow the steps in module 2 to enable the one-wire interface.
<br><br>
After enabling the one-wire interface you should be able to cd to the /sys/bus/w1/devices directory and see both of your sensors if every step was followed correctly. After you validate both of the sensors are visibile (2 id numbers in the directory), you can check the readings with  
 - cd 28-xxxxxx
 - cat w1_slave


## Python Script
For the project 4 script, you will need to read in the data from both the air and water temperature sesnor and display them to your lcd. Refer to the starter code for more details.
























