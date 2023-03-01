import RPi.GPIO as GPIO
import time

# Define the GPIO pin for the sound sensor
SOUND_PIN = 23

# Set up the sound pin as an input
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUND_PIN, GPIO.IN)

# Loop to detect sound
while True:
    # Check if sound is detected
    if GPIO.input(SOUND_PIN):
        print("Sound detected")
    else:
        print("No sound detected")
    # Wait for a short time to avoid excessive detection
    time.sleep(0.1)

# Clean up the GPIO pins
GPIO.cleanup()