import RPi.GPIO as GPIO
import time

def spin(angle):
    print("Spinning",angle)
    duty_cycle = 2.5 + (angle / 36) # Calculate the duty cycle based on the angle
    pwm.ChangeDutyCycle(duty_cycle)

SERVO_PIN = 18 # Define the GPIO pin for the servo signal
SMOOTHNESS = 2
SPEED = 0.005

#SETUP
GPIO.setmode(GPIO.BCM) # Set the GPIO mode to BCM
GPIO.setup(SERVO_PIN, GPIO.OUT)
pwm = GPIO.PWM(SERVO_PIN, 50) # Create a PWM instance with a frequency of 50 Hz
pwm.start(2.5) # Move the servo to the 0 degree position

while True:
    for angle in range(0, 361, SMOOTHNESS):
        spin(angle)
        time.sleep(SPEED)
    
    for angle in range(361, -1, SMOOTHNESS*-1):
        spin(angle)
        time.sleep(SPEED)

# Stop the PWM instance
pwm.stop()

# Clean up the GPIO pins
GPIO.cleanup()