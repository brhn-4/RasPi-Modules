
# Project 8: Interpret Sensor Data
Due: _________ at 11:59 PM <br>
Points: __________


## Introduction:
Now we're going to be working on the final part of the web project! So far we have successfully set up multiple sensors, created a web server, and read in that data to dynamically update our web page. Now we have to interpret that data. We're going to be using javascript to implement the functions we need as well as add a few elements to our DOM

<br><br>


## Coding:
For this portion of the project, you will continue to update the same web page you worked on in Module 7. Our goal for the last step is to add functionality that will alert the user if one of the parameters measured by our sensors is out of bounds (too high or too low). This application can run for a long time but the web page is also viewable even if app.py is not currently running so we also want to add an element to the DOM to let the viewer know how recent the data they are seeing is. Your tasks are as follows:

1. If the water temperature goes below 70F or above 85F turn the temperature reading red and send an alert to the user.
2. If the air temperature goes below 70F or above 85F turn the temperature reading red and send an alert to the user.
3. If the humidity reading is below 45% or above 60% turn the humidity reading red and send an alert to the user.
4. Only send the alert on the first reading for each parameter that goes out of bounds. (i.e if water temperature drops below 70F send an alert and only send another one if it goes back into the desired range and exits after)
5. Add a "Last Update" element that takes a time stamp and displays it for the user each time the readings are updated
6. Add the desired parameter range under the ideal parameter boxes





















