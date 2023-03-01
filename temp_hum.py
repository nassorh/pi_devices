import Adafruit_DHT

# Set the sensor type and GPIO pin number
SENSOR_TYPE = Adafruit_DHT.DHT22
GPIO_PIN = 13

# Loop to read the temperature and humidity values
while True:
    # Try to read the temperature and humidity values from the sensor
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR_TYPE, GPIO_PIN)
    print("Raw, ",humidity, temperature)
    # Print the values if they were successfully read
    if humidity is not None and temperature is not None:
        print('Temperature: {0:.1f}°C'.format(temperature))
        print('Humidity:    {0:.1f}%'.format(humidity))
    else:
        print('Failed to get reading. Try again!')

    # Wait a few seconds before reading again
    time.sleep(2)
