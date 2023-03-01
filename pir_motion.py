import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin for the PIR sensor
PIR_PIN = 17

# Set up the PIR pin as an input
GPIO.setup(PIR_PIN, GPIO.IN)

# Loop to detect motion
while True:
    # Check if motion is detected
    if GPIO.input(PIR_PIN):
        print(1) #Motion detected
    else:
        print(0) #No Motion detected
    # Wait for a short time to avoid excessive detection
    time.sleep(0.1)