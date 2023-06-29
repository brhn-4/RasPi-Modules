
# Project 2: Water Temperature
Due: _________ at 11:59 PM <br>
Points: __________


## Introduction
For this project, we will be connecting a water temperature sensor to our raspberry pi and outputting the values to the terminal. Our program will output both Celsius and Fahrenheit temperatures over time. This will be our first time attempting to get input from the GPIO pins and set the foundation for what we will be doing during the rest of this course. It is very important you get a good foundation of understanding the fundamentals for connecting these circuits in order to streamline future projects. As always make sure you ask questions if you are unsure of the wiring so as to not short-circuit the pi.
<br><br>
This project will be split into two parts wiring the sensor to your Pi and then writing a Python script to read the input. Depending on the state of your Pi's repository you may need to update certain packages. If you run into any unexpected issues make sure to double check everything is up to date and that you have installed the new packages correctly.
<br><br>
**HARDWARE REQUIREMENTS**: 1x ds18b20 sensor, 1x breakout board with 10k resistor, Jumper wires

## ds18b20
For this project, we will be using the ds18b20 water temperature sensor with an attached breakout board. This is a sealed digital temperature probe that measures precise temperatures in wet environments with an easy 1-Wire interface. The sensor itself has 3 different pins all color-coded and labeled. The 3 wires you see in the picture below are as follows: **Black -> Ground, Red -> VCC, and Yellow -> Data**.<br><br> Please note that if you have a different water temperature sensor this color code system may not be correct and you will have to check the specifications of that sensor to correctly wire it.

<p align="center">
  <img src="https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/1f0ed34e-6513-4e7a-bff8-abdc8ac93905" width="300" />
  <img src="https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/7d3926a5-c2f8-4e77-bfb8-7db7ed96f67a" width="300" /> 
</p>
<br><br>

## Connecting the Sensor

- **Step 1**: First you want to connect your sensor to the breakout board, you will need to make sure you are connecting the correct wires to the correct terminals on the breakout board otherwise you risk damaging the sensor. Additionally, you will need to take a small flathead screwdriver to secure the ends of the sensors wires into the breakout board. Refer to the image below for guidance.<br><br>  **Note:** If you do not have a breakout board with a resistor you will need to attach a 4.7K or 10k ohm resistor in between the data and VCC pins.
<p align="center">
  <img src="https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/403e6a49-deb1-4db5-b90f-cffeff06fa62" width="250" />
</p>

- **Step 2**: Now that everything is connected we need to attach it to the pi. Remember to disconnect power from your Pi before attaching anything.
- **Step 3**: First, connect the GND wire to any of the GND pins on the Pi or your breadboard. Then the VCCC wire to any 3.3V pin. Next, attach the Dat wire to any generic  GPIO. Refer to the image below for clarification on the wiring. 

<p align="center">
  <img src="https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/a1b1b886-4cfe-47b1-ba99-ff2b092d1aca" width="250" />
</p> 
<br>

**Note**: In the diagram above the breakout board is not shown and it is a slightly different version of the ds18b20. However, this circuit is wired the same as we want to wire ours. Additionally, it makes no difference which gnd, 3.3V, or Generic GPIO you choose or whether or not is directly inserted into the pi or into the breadboard

- **Step 4**: Now that we have connected our sensor to the Pi its time to power up the Pi and begin writing our Python script
<br>




## Software Configuration

We’ll need to enable the One-Wire interface before the Pi can receive data from our sensor. Once you have the sensor fully connected, the pi powered on, and you are logged in follow these steps to enable the One-Wire interface:
```
1. In the Pi's terminal enter 'sudo nano /boot/config.txt', then add 'dtoverlay=w1-gpio' to the bottom of the file:

    
2. Exit the config file then reboot the Pi with 'sudo reboot'. This may take a few seconds

3. Now, log in to your Pi again and in the terminal enter 'sudo modprobe w1-gpio'

4. Then enter 'sudo modprobe w1-therm'

5. cd to the directory '/sys/bus/w1/devices' 

6. Now enter ls to list the devices:

![module2 software config 1](https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/d72fd611-2438-475b-9489-de118c6347d6)

In my case, 28-000006637696 w1_bus_master1 is displayed.

7. Now enter cd 28-XXXXXXXXXXXX (with your own serial number)


8. Now, enter 'cat w1_slave' this will show the raw data our temperature sensor is reading:

![module2 software config 2](https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/64d555ea-77a9-4b53-9177-910d13f9c0f5)

```



## Python Script



















