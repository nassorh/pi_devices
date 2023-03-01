import time
import smbus2

# Define the DHT11 sensor address and register values
SENSOR_ADDR = 0x5c
TEMP_REGISTER = 0x00
HUMIDITY_REGISTER = 0x01

# Initialize the I2C bus
bus = smbus2.SMBus(1)

def read_sensor():
    # Send start signal to the sensor
    bus.write_byte(SENSOR_ADDR, 0x00)
    time.sleep(0.1)

    # Read 4 bytes of data from the sensor
    data = bus.read_i2c_block_data(SENSOR_ADDR, 0, 4)

    # Calculate temperature and humidity values
    humidity = data[HUMIDITY_REGISTER]
    temperature = data[TEMP_REGISTER]

    return temperature, humidity

# Read and print temperature and humidity data every second
while True:
    temperature, humidity = read_sensor()
    print(f"Temperature: {temperature}C, Humidity: {humidity}%")
    time.sleep(1)
