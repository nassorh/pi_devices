import RPi.GPIO as GPIO
from time import sleep
import time
import Adafruit_DHT
import threading 

class PiDevices:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)

    def cleanup(self):
        GPIO.cleanup()

    def __del__(self):
        self.cleanup()

class Button(PiDevices):
    def __init__(self, button_pin):
        super().__init__(button_pin)
        self.val = 0
        self.count = 0 #Record the number of button presses
        self.flag = 0 #Track whether its on or off
        GPIO.setup(button_pin, GPIO.IN, GPIO.PUD_UP)
        GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=self.button_callback)

    def button_callback(self, channel):
        self.count += 1

    def check_button(self):
        self.flag = self.count % 2
        print(self.flag,self.count)
        if self.flag == 1:
            return True
        return False

class Buzzer(PiDevices):
    def __init__(self, buzzer_pin):
        super().__init__(buzzer_pin)
        GPIO.setup(buzzer_pin, GPIO.OUT)

    def sound_alarm(self):
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(self.pin, GPIO.LOW)

class PIRSensor(PiDevices):
    def __init__(self, pir_pin):
        super().__init__(pir_pin)
        GPIO.setup(pir_pin, GPIO.IN)
        self.motion_detected = False
        self.thread = threading.Thread(target=self.detect_motion_thread)
        self.thread.daemon = True
        self.thread.start()

    def detect_motion_thread(self):
        while True:
            if GPIO.input(self.pin):
                self.motion_detected = True
            else:
                self.motion_detected = False
            time.sleep(0.1)

    def detect_motion(self):
        return self.motion_detected

class ServoMotor(PiDevices):
    def __init__(self, servo_pin, smoothness=2, speed=0.005):
        super().__init__(servo_pin)
        self.smoothness = smoothness
        self.speed = speed
        GPIO.setup(servo_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(servo_pin, 50) # Create a PWM instance with a frequency of 50 Hz
        self.pwm.start(2.5) # Move the servo to the 0 degree position

    def spin_(self, angle):
        duty_cycle = 2.5 + (angle / 36) # Calculate the duty cycle based on the angle
        self.pwm.ChangeDutyCycle(duty_cycle)

    def spin(self):
        for angle in range(0, 361, self.smoothness):
            self.spin(angle)
            time.sleep(self.speed)

        for angle in range(361, -1, self.smoothness*-1):
            self.spin(angle)
            time.sleep(self.speed)
    
    def cleanup(self):
        self.pwm.stop() 
        GPIO.cleanup()

class Temp_Hum(PiDevices):
    def __init__(self, dht_pin):
        super().__init__(dht_pin)
        self.temperature = None
        self.humidity = None
        self.thread = threading.Thread(target=self.read_values_thread)
        self.thread.daemon = True
        self.thread.start()

    def read_values_thread(self):
        sensor = Adafruit_DHT.DHT11
        while True:
            humidity, temperature = Adafruit_DHT.read_retry(sensor, self.pin)
            if humidity is not None and temperature is not None:
                self.temperature = temperature
                self.humidity = humidity
            else:
                self.temperature = None
                self.humidity = None
            time.sleep(2)

    def get_values(self):
        return self.temperature, self.humidity
