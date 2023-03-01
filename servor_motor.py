import RPi.GPIO as GPIO
import time

def spin(angle):
    pwm.ChangeDutyCycle(angle)

SERVO_PIN = 18 # Define the GPIO pin for the servo signal

#SETUP
GPIO.setmode(GPIO.BCM) # Set the GPIO mode to BCM
GPIO.setup(SERVO_PIN, GPIO.OUT)
pwm = GPIO.PWM(SERVO_PIN, 50) # Create a PWM instance with a frequency of 50 Hz
pwm.start(2.5) # Move the servo to the 0 degree position

degrees = [2.5, 7.5, 12.5] #2.5 = 0 deg, 7.5 = 90 deg, 12.5 = 180 deg
index = 1
while True:
    degree = degrees[index % len(degrees)]
    index += 1
    pwm.ChangeDutyCycle(degree)
    time.sleep(0.1)

#stop the PWM instance
pwm.stop()

# Clean up the GPIO pins
GPIO.cleanup()
