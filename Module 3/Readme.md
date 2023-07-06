
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

We’ll need to enable the I2C interface before we can begin interacting with our display. We also need to install Smbus and i2c-tools for our project which we will do during this phase. Once you have the LCD fully connected, the Pi powered on, and you are logged in follow these steps to enable the I2C interface and install the proper packages:

```
1. Type 'sudo raspi-config', This should open up a configuration menu.

2. Select 'Interfacing Options', Usually Option 5 

3. Select 'P5 I2C', then 'yes', and then 'finish'.   

4. Now restart your pi with 'sudo reboot'

5. You can now check whether or not it was installed by running 'lsmod | grep i2c'

6. You should see something like 'i2c_bcm2802 .........' if the instructions were run correctly

NOTE: If you have any issues typing ' | ' in the previous command this could be because your Pi is set to a UK keyboard layout. In the config menu, you can change this to the appropriate layout for whatever keyboard you are using

7. Next run 'sudo apt-get install i2c-tools', this will install I2C tools

8. Now run 'i2cdetect -y 1', if everything is working properly you will detect a device and see something like the output shown below

9. Now run 'sudo apt-get install python-smbus' and 'sudo apt-get install python3-smbus' to install Smbus
```
**I2C Detection**
<p align="center">
  <img src="https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/9bc39931-da31-4c94-9696-aab6f768fdc7" width="300" />
</p>



## Python Script






















