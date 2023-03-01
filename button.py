import RPi.GPIO as GPIO
from time import sleep

button = 26 #set buttonPin
val = 0 #Button variables
count = 0 #Record the number of button presses
flag = 0 #Odd even variable

#SETUP
GPIO.setmode(GPIO.BCM) # use BCM numbers
GPIO.setup(button,GPIO.IN,GPIO.PUD_UP) #set the buttonPin INPUT 

while True:
    val = GPIO.input(button) #Receive button value
    if(val == 0): #if button is pressed
        sleep(0.01) #Eliminate button jitter
        val = GPIO.input(button) #Receive button value
        if(val == 1): #Loosen the button
            count = count + 1 #Count the number of clicks on the
            print("count = %d" %count)
    flag = count % 2 #Remainder 2 ,Even is 0, odd is 1
    if(flag == 1):
        print("Button On")
    else:
        print("Button Off")

GPIO.cleanup() #release all GPIO