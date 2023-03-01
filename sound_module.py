import smbus
import time

I2C_BUS = 1
ADC_ADDR = 0x48
cmd = 0x40 #DA Convertor
bus = smbus.SMBus(I2C_BUS)
sensitivity = 10

def analogRead(count):
    #function,read analog data
    read_val = bus.read_byte_data(ADC_ADDR,cmd + count)
    return read_val

while True:
    ##loop
    value = analogRead(0) ##read A0 data
    if(value>sensitivity):
        print("Sound detected")
    else:
        print("No sound")
    time.sleep(0.05)
GPIO.cleanup()
