
########################################################################
# Filename    : Hello_World_Sol.py
# Description : Basic GPIO Input, Led On/Off
# Author      : brhn
# modification: 6/26/2023
########################################################################

from time import sleep

def h1():
    print('Hello World!')


def h2():
    word = 'Hello World'

    for i in word:
        print(i)
        sleep(0.5)

def h3():
    word = ['d','l','r','o','W',' ','o','l','l','e','H']
    n = len(word)
    for i in range(n,0,-1):
        print(word[i-1])
        sleep(0.5)





def destroy():

    quit()

if __name__ == '__main__':  ##Called on execution
    
    try:     #Try calling main function 'blink'
        print('executing h1...\n')
        sleep(2)
        h1()
        
        print('\nexecuting h2...\n')
        sleep(2)
        h2()
        
        print('\nexecuting h3...\n')
        sleep(2)
        h3()
    except KeyboardInterrupt:  #kill script
        destroy()
