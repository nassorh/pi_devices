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
    buzzer.sound_alarm(5) 
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

# Define the endpoint for turning on the servo motor
@app.route("/servo_on", methods=["POST"])
def servo_on():
    # Start the servo motor
    servo_motor.turn_on()
    # Redirect to the main page
    return "spinning"

# Define the endpoint for turning off the servo motor
@app.route("/servo_off", methods=["POST"])
def servo_off():
    # Stop the servo motor
    servo_motor.turn_off()
    # Redirect to the main page
    return "not spinning"

@app.route('/temp_hum')
def temp_hum_page():
    return render_template('temp_hum.html')

@app.route('/get_temp_hum')
def get_live_temp_hum():
    temperature, humidity = temp_hum.get_values()
    return jsonify({'temperature': temperature, 'humidity': humidity})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
