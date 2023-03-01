import spidev
import time

# Set the SPI bus and device
SPI_BUS = 0
SPI_DEV = 0

# Set the photoresistor channel on the MCP3008
PHOTO_RESISTOR_CHANNEL = 0

# Create an instance of the SPI object
spi = spidev.SpiDev()
spi.open(SPI_BUS, SPI_DEV)

# Define a function to read the photoresistor value from the MCP3008
def read_photoresistor():
    # Send the read command for the photoresistor channel
    # The first byte is 0b00000001 (start bit, single-ended mode, channel 0)
    # The second byte is 0b10000000 (null bit, null bit, null bit, null bit, MSB first)
    resp = spi.xfer2([0b00000001, 0b10000000, 0])
    
    # Combine the two bytes of the response into a single value
    photoresistor_value = (resp[1] << 8) + resp[2]
    
    return photoresistor_value

# Loop to read the photoresistor value
while True:
    photoresistor_value = read_photoresistor()
    print("Photoresistor value:", photoresistor_value)
    time.sleep(0.1)
