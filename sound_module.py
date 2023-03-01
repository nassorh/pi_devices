import RPi.GPIO as GPIO
import smbus
import time

# Define the analog pin to which the photoresistor is connected
ANALOG_PIN = A0

# Set up the ADC
address = 0x48
cmd = 0x40
bus = smbus.SMBus(1)

# Define a function to read the analog value from the specified pin
def analog_read(pin):
    read_val = bus.read_byte_data(address, cmd + pin)
    return read_val

# Loop to read the analog value from the photoresistor
while True:
    value = analog_read(ANALOG_PIN)
    print(value)
    time.sleep(0.1)
