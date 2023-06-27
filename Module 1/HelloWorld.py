
########################################################################
# Filename    : HelloWorld.py
# Description : Basic GPIO Input, Led On/Off
# Author      : brhn
# modification: 6/27/2023
########################################################################

from time import sleep

# INSTRUCTIONS:
# For this assignment you will need to complete 4 different tasks.
# 1. In the method h1() print 'Hello World!' to the console
#
# 2. In the method h2() print 'Hello World' one character at a time sleeping for .5 seconds in between each print
#
# 3. In the method  h3() print the contents of 'word' (which is 'Hello World' backwards) reversed so it outputs the same as h2() sleeping for the same time as h2()
#
# 4. Finish the destroy method to kill the script
# note: We have provided you with a main function that will be called upon execution. You will need to uncomment the method calls in the try block to test your methods
#       Check at the bottom for desired output

def h1(): 
   
def h2():
    word = 'Hello World'

def h3():
    word = ['d','l','r','o','W',' ','o','l','l','e','H']
   





def destroy():
    


if __name__ == '__main__':  ##Called on execution
    
    try:     #Try block calling main functions
        # print('executing h1...\n')
        # sleep(2)
        # h1()
        
        # print('\nexecuting h2...\n')
        # sleep(2)
        # h2()
        
        # print('\nexecuting h3...\n')
        # sleep(2)
        # h3()
    except KeyboardInterrupt:  #kill script
        destroy()
    
# CORRECT TERMINAL OUTPUT:
#
# executing h1...
# Hello World!
# excecuting h2...
# H
# e
# l 
# l 
# o 
 
# W 
# o 
# r 
# l 
# d 
# executing h3...
# H 
# e 
# l 
# l 
# o 
 
# W 
# o 
# r 
# l 
# d 
