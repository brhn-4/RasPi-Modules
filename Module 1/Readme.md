
# Project 1: Blink & Hello World
Due: _________ at 11:59 PM <br>
Points: __________

## Before You Start
Before starting this project, you should have completed Module 0. For this project, we will assume you have completed module 0 and correctly set up your Pi OS as well as an SSH connection if you do not have a display/keyboard directly connected to the Pi. Additionally, you will need a base knowledge of Python (or your preferred language) and command prompt commands/Linux.

## Introduction
For this project, we will be writing our first two Python scripts, as well as our first basic circuit. The two scripts will be "HelloWorld" which is the first program every computer scientist runs. We will be using this to verify you have Python installed properly on your pi, that you can access and run files via SSH, and to review how to create and execute Python scripts through the command prompt. After that, we will create our first circuit with an LED light and write a script that turns it on and off i.e blink. 

## Installing Python

Our first step will be installing Python on our machine. If you prefer to use a different language you will need to convert all starter code and the extensions to that language. You can install Python from the official website, through the command prompt, and even the terminal within Vscode
<br><br>

NOTE: For the remainder of the module we will refer to many Linux commands executed on the Raspberry Pi through our SSH connection. You can access Linux in many ways including VsCode. If you are not using Linux make sure to find similar commands online
<br><Br>
**Instructions**
```
  Ctrl+`  #Open terminal in Vscode

  Now Run the following commands:

 'sudo apt update' #update your system's repository
 'sudo apt install python3' #install python 3
 'python3 --version' #check what version was installed, update if necessary
 'python3' #if this runs without error you will know you have installed python!
 'quit()' #this will kill the Python shell 
```




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

  















