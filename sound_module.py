import RPi.GPIO as GPIO
import smbus
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 5
GPIO.setup(led,GPIO.OUT)
address = 0x48
cmd = 0x40
A0 = 0x40
A1 = 0x41
A2 = 0x42
A3 = 0x43
bus = smbus.SMBus(1)

##start the bus
def analogRead(count): #function, read analog data
    read_val = bus.read_byte_data(address,cmd + count)
    return read_val

while True:
    value = analogRead(0) ##read AO data
    print(value)
