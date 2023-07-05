
# Project 3: LCD
Due: _________ at 11:59 PM <br>
Points: __________


## Introduction
For this project, we will be connecting an LCD to our Pi to display the readings from our temperature sensor
<br><br>
This project will be split into two parts wiring the LCD to your Pi and then writing a Python script to read the input. Depending on the state of your Pi's repository you may need to update certain packages. If you run into any unexpected issues make sure to double check everything is up to date and that you have installed the new packages correctly.
<br><br>
**HARDWARE REQUIREMENTS**: 1x I2C LCD1602, Jumper wires

## I2C LCD1602
For this project, we are going to be connecting a display to our Pi that will be able to show the values from our ds18b20 sensor from Module 2 rather than outputting it to the terminal as before. There are multiple types of LCD1602 displays. One of which has a 16-pins and the I2C LCD which we will be using has 4. If you are not using the I2C LCD1602. You will need to refer to an online tutorial to connect the display, however, the Python script should be relatively the same (you will need to access the data differently but the rest will be the same).

<br><br>

## Connecting the Sensor
NOTE: Because, as stated earlier we only need 4 pins to control the 16 pins of the LCD1602 Display Screen through the I2C interface. Reference the schematic diagram below for clarification.

<p align="center">
  <img src="https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/8c6eab57-d3c9-43af-b147-baeaaf5cfbe7" width="300" />
</p>

- **Step 1**: First, like always you want to disconnect the power supply from your pi.
- **Step 2**: Secondly, connect the GND (black) pin of the LCD to any of the GND pins in the pi or breadboard. NOTE: If you look on the top of your LCD there should be labeling to identify which pin is which, or refer to the schematic.
- **Step 3**: Connect the VCC (red) to the 5v pin
- **Step 4**: Connect the SDA (yellow) to the SDA GPIO pin (pin 3)
- **Step 5**: Connect the SCL (blue) to the SCL GPIO pin (pin 5)
- **Step 6**: Now that everything is connected we can re-connect our Pi to power, connect and begin writing our Python script

<p align="center">
  <img src="https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/b508481a-e04e-4d97-b29e-a30babcb91f7" width="300" />
</p>


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






















