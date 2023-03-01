import RPi.GPIO as GPIO
import time

def spin(angle):
    duty_cycle = 2.5 + (angle / 18.0) # Calculate the duty cycle based on the angle
    pwm.ChangeDutyCycle(duty_cycle)

SERVO_PIN = 18 # Define the GPIO pin for the servo signal

#SETUP
GPIO.setmode(GPIO.BCM) # Set the GPIO mode to BCM
GPIO.setup(SERVO_PIN, GPIO.OUT)
pwm = GPIO.PWM(SERVO_PIN, 50) # Create a PWM instance with a frequency of 50 Hz
pwm.start(2.5) # Move the servo to the 0 degree position

degrees = list(range(25, 126, 1)) # Define a range of degrees to sweep through
index = 0 # Start at the first value in the list
direction = 1 # 1 for forward, -1 for backward

while True:
    # Spin the servo motor through 0 to 180 degrees
    for angle in range(0, 181, 10):
        spin(angle)
        time.sleep(0.5)

    # Spin the servo motor back through 180 to 0 degrees
    for angle in range(180, -1, -10):
        spin(angle)
        time.sleep(0.5)

# Stop the PWM instance
pwm.stop()

# Clean up the GPIO pins
GPIO.cleanup()