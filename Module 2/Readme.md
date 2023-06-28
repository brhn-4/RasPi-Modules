

# Project 2: Water Temperature
Due: _________ at 11:59 PM <br>
Points: __________


## Introduction
For this project, we will be connecting a water temperature sensor to our raspberry pi and outputting the values to the terminal. Our program will output both Celsius and Fahrenheit temperatures over time. This will be our first time attempting to get input from the GPIO pins and set the foundation for what we will be doing during the rest of this course. It is very important you get a good foundation of understanding the fundamentals for connecting these circuits in order to streamline future projects. As always make sure you ask questions if you are unsure of the wiring so as to not short-circuit the pi.
<br><br>
This project will be split into two parts wiring the sensor to your Pi and then writing a Python script to read the input. Depending on the state of your Pi's repository you may need to update certain packages. If you run into any unexpected issues make sure to double check everything is up to date and that you have installed the new packages correctly.
<br><br>
HARDWARE REUQIREMENTS: 1x ds18b20 sensor, 1x breakout board with 10k resistor, Jumper wires

## DS18b20
For this project, we will be using the ds18b20 water temperature sensor with an attached breakout board. This is a sealed digital temperature probe that measures precise temperatures in wet environments with an easy 1-Wire interface. The sensor itself has 3 different pins all color-coded and labeled. The 3 wires you see in the picture below are as follows: **Black -> Ground, Red -> VCC, and Yellow -> Data**.<br><br> Please note that if you have a different water temperature sensor this color code system may not be correct and you will have to check the specifications of that sensor to correctly wire it.

<p align="center">
  <img src="https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/1f0ed34e-6513-4e7a-bff8-abdc8ac93905" width="300" />
  <img src="https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/7d3926a5-c2f8-4e77-bfb8-7db7ed96f67a" width="300" /> 
</p>
<br><br>

## Connecting the Sensor

- **Step 1**: First you want to connect your sensor to the breakout board, you will need to make sure you are connecting the correct wires to the correct terminals on the breakout board otherwise you risk damaging the sensor. Refer to the image below for guidance.  **Note:** If you do not have a breakout board with a resistor you will need to attach a 4.7K or 10k ohm resistor in between the data and VCC pins.
<p align="center">
  <img src="https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/403e6a49-deb1-4db5-b90f-cffeff06fa62" width="250" />
</p>

- **Step 2**: Now that everything is connected we need to attach it to the pi. Remember to disconnect power from your Pi before attaching anything.
- **Step 3**: First, connect the GND wire to any of the GND pins on the Pi or your breadboard. Then the VCCC wire to any 3.3V pin. Next, attach the DAt wire to any generic  GPIO. Refer to the image below for clarification on the wiring. 


![ds18b204](https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/192736c0-a34d-4d5b-b15a-a622cc9d2b66)




## Hello World
Now we are going to be writing our first Python script 'Hello World'. Inside this module, there is a file called "HelloWorld.py". We will try out 3 different exercises to review some Python skills. <br><br>
For this exercise complete each of the three commented-out blocks one by one. Once you have finished one of them execute the file by running "python3 HelloWorld.py". Validate the output and then kill the script with "Ctrl+C". 


## Blink 
For the next portion, we will be constructing our first circuit and writing another Python script to control it. The circuit will be a simple LED light that we will control with our pi by executing a script to make the light blink. First, we will construct the circuit.
<br><br>
WARNING: When working with circuits it is important to be very careful as connecting the wrong components to the wrong pins, using the incorrect voltage, or not adding enough resistance can cause serious damage to both the component and the raspberry pi. <br><br>To be safe make sure whenever you edit anything on your breadboard or connected to the pi there is no power in the pi (unplug it). Additionally, always double check you have a good connection (i.e. the jumper cable/LED/sensor is fully plugged in). Lastly, always double check you are connecting the cables to the correct pins. If you do not have a GPIO extension board, it may be helpful to reference the image of the GPIO layout below when assembling your circuit.

<p align="center">
<img  width=auto height='450' src='https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/8635543b-0f53-431c-a52e-25c177d05dc4'>
</p>

### Hardware Used:

<p align="center">
<img  width=auto height='150' src='https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/b1541db1-75eb-4fbf-9f51-f680d108645e'>
</p>

### Circuit:

<p align="center">
<img  width=auto height='300' src='https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/70b3c702-657a-4742-aa4f-9378531059e1'>
</p>

CAUTION: Avoid any possible short circuits (especially connecting 5V or GND, 3.3V and GND)!
WARNING: A short circuit can cause high current in your circuit, create excessive component heat and cause
permanent damage to your RPi!


### Code:
For the Blink script, you will have 3 main tasks. Assigning the proper GPIO to the variable 'led', creating a continuous blink that switches on and off every second until instructed to terminate from a keyboard interrupt, and creating a method for 5 long blinks. Refer to the starter code for more details.

  















