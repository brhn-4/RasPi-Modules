# Project 7: Web IOT
Due: _________ at 11:59 PM <br>
Points: __________


## Introduction
If you have completed the previous modules and continued on to this one you are now done with the hardware portion of the projects. Throughout this project, we have been designing a water monitoring/control system. But, we have only been displaying our data on a small LCD so far. In the second half of the project that we are now going to begin, we will be doing something different.
<br><br>
Now that we have a way to read in data from all of our sensors we are going to be doing 3 main tasks. Designing an HTML/CSS/Js web server, sending data from the raspberry pi over the internet to this web server, and finally interpreting the data dynamically on our web server
<br><br>
Accomplishing these three tasks could take a long time so we will again be splitting it up into modules. In this module, we will show you how to set up your own webserver and give you an outline of what you will need when designing it with HTML/CSS/Js.

<br><br>
## Web Server





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
























