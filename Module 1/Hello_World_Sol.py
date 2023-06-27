
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
    for i in range(n,-1,-1):
        print(word[i-1])
        sleep(0.5)





def destroy():
    print('Program ending...')
    quit()

if __name__ == '__main__':  ##Called on execution
    
    try:     #Try calling main function 'blink'
        print('executing h1...\n')
        h1()
        sleep(3)
        print('executing h2...\n')
        h2()
        sleep(3)
        print('executing h3...\n')
        h3()
    except KeyboardInterrupt:  #kill script
        destroy()
