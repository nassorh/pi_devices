import RPi.GPIO as GPIO
import time

buzzer_pin = 26

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)
# Set up the PIR pin as an input
GPIO.setup(buzzer_pin, GPIO.IN)

while True:
    GPIO.output(buzzer_pin,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(buzzer_pin,GPIO.LOW)

GPIO.cleanup()