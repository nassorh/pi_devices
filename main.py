from flask import Flask, render_template,jsonify,request
from pi_devices import Button, Buzzer, PIRSensor, ServoMotor, Temp_Hum

app = Flask(__name__)

# Initialize PiDevices
button = Button(23)
buzzer = Buzzer(26)
pir_sensor = PIRSensor(17)
servo_motor = ServoMotor(18)
temp_hum = Temp_Hum(13)

# Create routes for each feature
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button')
def button_page():
    return render_template('button.html')

@app.route('/get_button_state')
def get_button_state():
    button_state = 'On' if button.check_button() else 'Off'
    return button_state

@app.route('/buzzer')
def buzzer_page():
    return render_template('buzzer.html')

@app.route('/sound_buzzer')
def sound_buzzer():
    duration = request.args.get('duration', default=5, type=int) # get the input value, default to 5 if not provided
    buzzer.sound_alarm(duration) 
    return 'Buzzer sounded for {} seconds!'.format(duration)

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
    return render_template('temp_hum.html')

@app.route('/get_temp_hum')
def get_live_temp_hum():
    temperature, humidity = temp_hum.get_values()
    return jsonify({'temperature': temperature, 'humidity': humidity})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
