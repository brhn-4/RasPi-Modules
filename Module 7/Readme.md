# Project 7: Web IOT
Due: _________ at 11:59 PM <br>
Points: __________


## Introduction:
If you have completed the previous modules and continued on to this one you are now done with the hardware portion of the projects. Throughout this project, we have been designing a water monitoring/control system. But, we have only been displaying our data on a small LCD so far. In the second half of the project that we are now going to begin, we will be doing something different.
<br><br>
Now that we have a way to read in data from all of our sensors we are going to be doing 3 main tasks. Designing an HTML/CSS/Js web server, sending data from the raspberry pi over the internet to this web server, and finally interpreting the data dynamically on our web server
<br><br>
Accomplishing these three tasks could take a long time so we will again be splitting it up into modules. In this module, we will show you how to set up your own web server and give you an outline of what you will need when designing it with HTML/CSS/Js.

<br><br>
## Web Server:
Our first goal is to set up a web server with our raspberry pi. This will allow us to create a page that any device on the same wifi will be able to access. This can be done very easily by using Apache2. Follow the steps below to set up the web server.
<br>
`````````
 sudo apt update
 sudo apt install apache2 -y
 sudo apt install php libapache2-mod-php -y

 **Now we have the proper packages installed for our server we need to change the ownership**

cd /var/www/html    -you should see index.html in this directory
ls -al              -here you can see 'root' owns index.html
sudo chown [user]: index.html    -add your user to the command to change the ownership
`````````

<br><br>

After finishing those commands it's time to test out our webserver. On your personal device try typing your pi's ip address i.e. 10.0.0.51. If your webserver was set up correctly this should pull up the apache2 home page on any of your devices. 






## Designing a Web Page:

Now that we have established our web server. It's time to design it! While there are many ways to design pages for the rest of the project we will be referring to HTML/CSS/Js. We strongly recommend the use of those languages for compatibility with the provided starter code. <br><br>

Html, CSS, and js aren't exactly programming languages on their own but instead, all weave together to create a web page. Html refers to the physical elements and DOM (Document Object Model) of the page, you can think of this as what creates the boxes, images, links, and text on a page. CSS is a styling component that allows you to change colors, fonts, sizes, positioning, or other things like that. Js or javascript handles the functionality of the page, this refers to things like buttons, functions, searches, and any other functionality within the page. <br><br>

There are many ways to weave these together beautifully to create amazing web pages. While getting familiar with these languages we have two recommendations. Firstly, using external js and CSS. External js/CSS means keeping all of your js and CSS in separate files, then all you need to do is add one line of code at the top of your HTML page to link it. This drastically helps clean up your code and keep things organized. Secondly, we recommend using Bootstrap. Bootstrap is a module that contains lots of built-in HTML/CSS/js to make your life easier. You can link multiple style or js pages in your HTML document and to use Bootstrap all you have to do is link it as well. Below we have provided a few helpful links to help you get started.
<br><br>

# Helpful Resources
After taking a look at these resources you will start designing the webpage

- https://www.w3schools.com/html/
- https://www.w3schools.com/css/
- https://www.w3schools.com/js/
- https://getbootstrap.com/

## Coding:

Now it's time to implement our web page on the web server we established. This is more of an open-ended assignment and the way you choose to organize your DOM and style your page is up to you but must make sense within the context. 
<br><br>
Your end task for this web page will be a page that reads in the data from our sensors updates the webpage with the current data every X minutes and alerts the users whether or not the data is within the given parameters. For this module, we will simply be designing the page. The next two modules will handle fetching the data and interpreting it.
<br><br>
In the starter code, you have 3 files: home.html, style.css, and funcs.js. It is up to you whether or not you use internal, external, or in-line js/css but the files are there and linked for your convenience. 
<br><br>

For this portion of the assignment, your tasks are as follows:

1. Create a floating top banner (nav bar)
2. Implement a live clock (that reads from your pc) in the top banner
3. One main element that will have sections for each sensor labeled and a title reading: 'Latest Update'
4. A second main div with identical labels but titled: 'Ideal Parameter' and underneath the labels for each sensor the ideal range for the data


















