
# Project 4: Air Temp
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
  <img src="https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/34c08cea-4f2f-4dc3-9ff2-2082bd733bc4" width="300" />
</p>



## Connecting the Sensor


<p align="center">
  <img src="https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/8c6eab57-d3c9-43af-b147-baeaaf5cfbe7" width="300" />
</p>

- **Step 1**: First, like always you want to disconnect the power supply from your pi.
- **Step 2**: Secondly, connect the GND (black) pin of the LCD to any of the GND pins in the pi or breadboard. NOTE: If you look on the top of your LCD there should be labeling to identify which pin is which, or refer to the schematic.
- **Step 3**: Connect the VCC (red) to the 5v pin
- **Step 4**: Connect the SDA (yellow) to the SDA GPIO pin (pin 3)
- **Step 5**: Connect the SCL (blue) to the SCL GPIO pin (pin 5)
- **Step 6**: Now that everything is connected we can re-connect our Pi to power, connect and begin writing our Python script




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























