import smbus
import time

I2C_BUS = 1
ADC_ADDR = 0x48
bus = smbus.SMBus(I2C_BUS)

flag = 0
mode = 0

def analogRead(count):
    #function,read analog data
    read_val = bus.read_byte_data(address,cmd + count)
    return read_val

while True:
    ##loop
    value = analogRead(0) ##read A0 data
    if(value>50):
        flag += 1
        mode = flag % 2
    print("data:%1.Of" %(value))
    time.sleep(0.05)
GPIO.cleanup()

# # Set the I2C bus number (0 or 1)
# I2C_BUS = 1

# # Set the I2C address of the ADC
# ADC_ADDR = 0x48

# # Create an instance of the I2C bus object
# i2c = smbus.SMBus(I2C_BUS)

# # Define a function to read the ADC value from a given channel
# def read_adc(channel):
#     # Send the channel number to the ADC
#     i2c.write_byte(ADC_ADDR, channel)
    
#     # Read the ADC value (two bytes, MSB first)
#     msb = i2c.read_byte(ADC_ADDR)
#     lsb = i2c.read_byte(ADC_ADDR)
    
#     # Combine the two bytes into a single 10-bit value
#     adc_value = (msb << 8) | lsb
    
#     return adc_value

# # Loop to read the ADC value from channel 0
# while True:
#     adc_value = read_adc(0)
#     print("ADC value:", adc_value)
#     time.sleep(0.1)
