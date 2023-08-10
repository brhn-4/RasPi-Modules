
# Project 8: Display Sensor Data
Due: _________ at 11:59 PM <br>
Points: __________


## Introduction:
Now that we have created our web page framework, it's time to read in the data from our sensors. To combine our existing Python script with our new web page we will be using Flask and AJAX. This will give us the ability to call our Python script at a set interval of time and dynamically update our web page with new content.
<br><br>
## Flask / AJAX:
Now we are going to read in our data using Flask and AJAX. Flask is a lightweight and micro web framework for Python, enabling developers to easily create web applications by providing the necessary tools and libraries for handling HTTP requests and rendering templates. AJAX (Asynchronous JavaScript and XML) is a technique used in web development that allows a web page to communicate with the server asynchronously, without refreshing the whole page, leading to a more dynamic and responsive user experience. In a Flask application, AJAX can be implemented using JavaScript to make asynchronous requests to the server, sending or retrieving data in the background. Flask handles these AJAX requests on the server side by defining specific routes or endpoints that process the incoming data, execute logic, and return a response, typically in JSON format. Together, Flask and AJAX enable the creation of modern and interactive web applications, with Flask taking care of the server-side logic and AJAX handling seamless client-server communication. By using Flask with AJAX, developers can build applications that provide users with immediate feedback, creating a more engaging and user-friendly interface.
<br><br>

# Software Configuration:
To install Flask run:
`````````
sudo apt update
pip install Flask
pip install Flask-CORS
`````````
<br><br>
To include AJAX add "<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>" to the head of your web page

## Coding:
For this portion of the project, you will be updating the same file you previously worked on. In the starter code for that module, there is a commented-out outline for an AJAX fetch request, that should help you start implementing the requirements for this module. The requirements are as follows:

1. Successfully read in water temperature formatted to two decimal points
2. Successfully read in air temperature formatted to two decimal points
3. Successfully read in humidity formatted to one decimal point
4. Successfully read in water flow formatted to one decimal point
5. Update data every 10 seconds





















