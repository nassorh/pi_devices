import spidev
import time

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)

# Function to read analog value from ADC
def read_adc(adc_channel):
    adc = spi.xfer2([1, (8 + adc_channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

# Main loop
while True:
    # Read analog value from photoresistor on channel 0
    photo_value = read_adc(0)
    
    # Print the analog value to console
    print("Photoresistor value:", photo_value)
    
    # Delay for a short period of time
    time.sleep(0.1)
