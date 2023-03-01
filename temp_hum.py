import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)

def read_adc(channel):
    adc = spi.xfer2([1, (8+channel)<<4, 0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

def convert_temp(data):
    temp = (data * 3.3 / 1024.0) * 100
    return round(temp, 1)

try:
    while True:
        temp_data = read_adc(0)
        print("raw",temp_data)
        temp = convert_temp(temp_data)
        print("Temperature: {}C".format(temp))
        time.sleep(1)

except KeyboardInterrupt:
    spi.close()
