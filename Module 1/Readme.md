
# Project 0: Raspberry Pi Introduction
Due: _________ at 11:59 PM <br>
Points: __________

## Before You Start
During this phase, we will be assembling our raspberry pi, setting up our OS or _Operating System_, and establishing an SSH connection to the raspberry pi. Assembling the computer and installing the proper software is crucial for success in further modules and ensuring everything is working properly. Therefore it is critical to follow the directions as closely as possible and ask questions when confused. 

## Introduction
[Raspberry Pi][rasPi] is a small single-board computer that is capable of doing everything you’d expect a desktop computer to do, from browsing the internet and playing high-definition video, to making spreadsheets, and even interpreting data from sensors interacting with the real world. For the remainder of this course, we will be focusing on interacting with sensors to gather and analyze data in hopes to create a water control system. Our first step in this process is to set up our raspberry pi and connect to it. 

## Assembling The Raspberry Pi 
<p align="center">
<img  width=auto height='400' src='https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/446f37a2-55ea-4c25-a471-6f16c2654e13'>
</p>
Firstly, if you are taking your Pi out of the box there is some assembly required. If your Pi does not have all of its parts attached (i.e. Heat Sinks) you want to do that at this time. Additionally, if you have a case for your Pi and want to assemble that and install the Pi you should do that at this time. 
<br><br>

NOTE: While many cases are good for protecting the Pi from physical damage and storing the Pi, you will need a case that has an open top or easy access to the GPIO pins to complete most of the projects. If your case obstructs access to the pins, you can either discard the case during this project or leave the top off. 


## Setting up the OS
Now we are going to set up the Raspberry Pi operating system on our Pi. During these next few steps, we will be installing the entire operating system as well as configuring our Pi to support an SSH connection.<br><br> It is important to note that there are two different ways to set up our Pi. The first is the more straightforward way of connecting a display to our Pi. The second is called a "Headless Setup" meaning we do all of the configuration with no display or keyboard. The following steps will be separated into those categories. Additionally, many Raspberry Pi's come with the operating system already installed on their SD card, which will allow you to skip a few steps.<br><br>
<b>NOTE HARDWARE SPECIFICATIONS:</b>
<br>
- **Power Supply**: We recommend the official Raspberry Pi Power Supply, which has been specifically designed to consistently provide +5.1V despite rapid fluctuations in current draw. For the Raspberry Pi 4 Model B and Raspberry Pi 400, you should use the type C power supply; for all other models, you should use the micro USB power supply.
- **SD Card**: If your Pi does not come with an SD card, we recommend a minimum of 8GB micro SD card and using the Raspberry Pi Imager to install an operating system onto it.
- **Display**: The Raspberry Pi 4 has two micro HDMI connectors, which require a good-quality micro HDMI cable, especially when using 4K monitors or television.


### Non-Headless Setup
- **Step 1**: Connect your display (monitor/touchscreen), keyboard, and mouse. The display will connect to the micro HDMI port on the Pi. The mouse (which can be Bluetooth) and keyboard both should connect to a USB port on the Pi. If you are unfamiliar with the ports, refer to the labeled picture above for clarity.
- **Step 2**: If your SD card already has the OS written on it you're done and can skip down to the SSH steps! Otherwise, we need to install the OS with Raspberry Pi Imager. Download it [here][imager].
<p align="center">
<img  width=auto height='400' src='https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/57b7d4d8-0d60-4315-b8c4-d8bf7f2fcb04'>
</p>

- **Step 3**: Insert the SD card into your laptop and open Imager
- **Step 4**: Select the proper OS (Raspberry PI OS 32/64 bit). *Make sure you check if you have a 32-bit or 64-bit pi
- **Step 5**: Choose the SD card you inserted as the storage
- **Step 6**: Hit write and then verify. It may take a few minutes to install this.
- **Step 7**: Once it is finished installing insert your SD card back into the Pi and you're done!

### Headless Setup
Here we are going to walk you through a headless setup of the raspberry pi, meaning you have no display or keyboard connected to your Raspberry Pi. To achieve this we are going to put the SD card for the Raspberry Pi into our laptop or desktop. This will allow us to write configuration specifications that will connect the Pi to wifi and install the OS onto the Pi when we re-insert the SD card into it. Once it is connected to the wifi our laptop will be able to SSH (Secure Shell Access) to the Pi and control it from our laptops through the wifi. Think of it as connecting the Pi to your laptop and then being able to use your laptop's screen and keyboard to control the Pi.
<br><br>
NOTE: While the headless setup may seem tedious and more complex than connecting a display and keyboard to the Pi, this is actually the standard method as once we establish an SSH connection we are able to eliminate the need for an auxiliary display/keyboard and use our more familiar machine to operate the pi (our laptops/desktops)
- **Step 1**: Install imager onto your PC.  Download it [here][imager]. 
- **Step 2**: Insert your SD card into your PC and open imager. (check hardware specifications for SD specifications)
- **Step 3**: For our configuration, under "Operating System",  select the proper OS (Raspberry PI OS 32/64 bit). *Make sure you check if you have a 32-bit or 64-bit pi. NOTE: if your SD card already has the proper OS installed you can skip this step.
- **Step 4**: For "Storage" select the inserted SD card.
  
- **Step 5**: Now click the settings button in the bottom right corner or hit CTRL + Shift + X to bring up the settings menu
- **Step 6**: Toggle set hostname and change the hostname if you want your device to be named anything other than "raspberrypi."
  
<p align="center">
<img  width=auto height='400' src='https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/9fb9f6be-2069-4cdb-90fe-65e2370c1707'>
</p>

- **Step 7**: Toggle enable SSH to on and select "User password authentication."

<p align="center">
<img  width=auto height='400' src='https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/958482c4-0d0c-4e86-8687-7c08f5f7b9d3'>
</p>

- **Step 8**: Set a username and password for your Pi. Note that if you use the password "raspberry" with username "pi," you may get a warning message when you log in, recommending (but not forcing you) that you change the password.
  
<p align="center">
<img  width=auto height='400' src='https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/f64d2f41-c269-4b5c-9bbe-9eab1959e453'>
</p>

<br><br>
  NOTE: If you are able to directly connect the Pi directly to the wireless internet via ethernet cable you can skip the following Wifi configuration
  
- **Step 9**: Set your Wi-Fi network's SSID, password and country. Then click Save. The country usually defaults to "GB" (Great Britain) so you will need to scroll down to set it to US.

<p align="center">
<img  width=auto height='400' src='https://github.com/brhn-4/INTAG-RasPi-Modules/assets/71796616/863d26d1-90f2-478e-8563-a74e6f783c78'>
</p>

- **Step 10**: Now save your configuration settings and write to the SD card. This may take a few minutes to install. Once it is finished remove it from your PC and insert it into the Pi

  














