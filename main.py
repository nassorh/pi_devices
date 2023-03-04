from flask import Flask, render_template
from pi_devices import Button, Buzzer, PIRSensor, ServoMotor, Temp_Hum

app = Flask(__name__)

# Initialize PiDevices
button = Button(23)
buzzer = Buzzer(26)
pir_sensor = PIRSensor(13)
servo_motor = ServoMotor(18)
dht11_sensor = DHT11Sensor(4)

# Create routes for each feature
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button')
def button_page():
    return render_template('button.html')

@app.route('/get_button_state')
def get_button_state():
    button_state = 'Pressed' if button.check_button() else 'Not pressed'
    return button_state

@app.route('/buzzer')
def buzzer_page():
    return render_template('buzzer.html')

@app.route('/sound_buzzer')
def sound_buzzer():
    buzzer.sound_alarm()
    return 'Buzzer sounded!'

@app.route('/pir')
def pir_page():
    return render_template('pir.html')

@app.route('/get_pir_state')
def get_pir_state():
    pir_state = pir_sensor.motion_detected
    return str(pir_state)

@app.route('/servo')
def servo_page():
    return render_template('servo.html')

@app.route('/toggle_servo')
def toggle_servo():
    if servo_motor.check_on():
        servo_motor.off()
        return 'Servo motor turned off!'
    else:
        servo_motor.on()
        return 'Servo motor turned on!'

@app.route('/temp_hum')
def temp_hum_page():
    temperature, humidity = dht11_sensor.get_values()
    return render_template('temp_hum.html', temperature=temperature, humidity=humidity)

@app.route('/get_temp_hum')
def get_live_temp_hum():
    temperature, humidity = dht11_sensor.get_values()
    return jsonify({'temperature': temperature, 'humidity': humidity})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
