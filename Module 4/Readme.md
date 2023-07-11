
# Project 4: Air Temperature
Due: _________ at 11:59 PM <br>
Points: __________


## Introduction
For this project, we are going to be connecting another ds18b20 sensor. However, this time we going to use an air temperature sensor. After we connect our new temperature sensor we are going to incorporate the two previous projects by having our LCD display both the water and the air temperature.
<br><br>
This project will be split into two parts wiring the sensor to your Pi and then writing a Python script to read the input. Depending on the state of your Pi's repository you may need to update certain packages. If you run into any unexpected issues make sure to double check everything is up to date and that you have installed the new packages correctly.
<br><br>
**HARDWARE REQUIREMENTS**: 1x ds18b20 air temperature sensor, 1x 4.7k ohm resistor, Jumper wires


<br><br>
## ds18b20
For this project, we will be using another ds18b20 temperature sensor except without an attached breakout board like late time. The sensor itself has 3 different pins VCC, Ground, and Data. Please check on the sensor itself or the image below for reference as to which pin is which.
<p align="center">
  <img src="https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/34c08cea-4f2f-4dc3-9ff2-2082bd733bc4" width="350" />
</p>



## Connecting the Sensor

Now when we are connecting the sensor we will have to re-wire our water temperature to create one circuit with both of the sensors that we connect to the Pi. 


- **Step 1**: First, like always you want to disconnect the power supply from your pi.
- **Step 2**: Secondly, connect the GND (black) pins of both the sensors to the negative rail of your breadboard. 
- **Step 3**: Now connect the VCC (red) pins to the positive rail of your breadboard.
- **Step 4**: Connect the negative rail to the GND GPIO pin of your raspberry pi
- **Step 5**: Connect the postitive rail to the 3.3V GPIO pin
- **Step 6**: Connect all 3 Data pins to one column on the bread board
- **Step 7**: Connect the postiive rail to a seperate column on the bread board
- **Step 8**: Connect a 4.7k Ohm resistor in between the two columns
- **Step 9**: Now connect a seperate wire after the resistor from the Data column to a generic GPIO
- **Step 8**: Now that everything is connected we can power on our pi and begin coding!

  NOTE: Refere to the diagram below for clarification. The diagram showcases 3 ds18b20 air temp sensors to show how to add more after the second sensor. Simply ignore the third sensor in the diagram. Additonally, there is no difference between the water and air temperature sensors when wiring.

<p align="center">
  <img src="https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/dc11e5aa-390a-4002-ba7b-10a9567da1cf" width="300" />
</p>


## Software Configuration

We’ll need to enable the One-Wire interface before the Pi can receive data from our sensor if you didn't already in module 2. Once you have the sensor fully connected, the pi powered on, and you are logged in follow the steps in module 2 to enable the one-wire interface.
<br><br>
After enabling the one-wire interface you should be able to cd to the /sys/bus/w1/devices directory and see both of your sensors if every step was followed correctly. After you validate both of the sensors are visibile (2 id numbers in the directory), you can check the readings with  
 - cd 28-xxxxxx
 - cat w1_slave


## Python Script
For the project 4 script, you will need to read in the data from both the air and water temperature sesnor and display them to your lcd. Refer to the starter code for more details.























