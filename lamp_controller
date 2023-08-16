import paho.mqtt.client as mqtt
import logging
import configparser
from lamp_logic import handle_motion

config = configparser.ConfigParser()
config.read('lamp_logic_config.ini')

MQTT_BROKER = config['DEFAULT']['MQTT_BROKER']
MQTT_PORT = int(config['DEFAULT']['MQTT_PORT'])
LOG_FILE_PATH = config['DEFAULT']['LOG_FILE_PATH']

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename=LOG_FILE_PATH,
                    filemode='a')

current_states = {}  # A dictionary to hold the state (on/off) for each lamp

def on_connect(client, userdata, flags, rc):
    logging.info(f"Connected to MQTT broker with code: {rc}")
    for section in config.sections():
        client.subscribe(config[section]['MQTT_TOPIC'])

def on_message(client, userdata, msg):
    logging.info(f"Received message '{msg.payload}' on topic '{msg.topic}'")
    
    for sensor in config.sections():
        if msg.topic == config[sensor]['MQTT_TOPIC']:
            affected_sensor, action = handle_motion(sensor, config, current_states)
            
            # Update the lamp's state and the current_states dictionary
            control_lamp(config[affected_sensor]['LAMP_IP'], action)
            current_states[affected_sensor] = action

def control_lamp(ip, action):
    logging.info(f"{'Turning ON' if action else 'Turning OFF'} the lamp with IP address {ip}!")
    lamp_set_state(ip, action)

def lamp_set_state(ip_address, turn_on=True):
    # Your pseudo function to control the lamp using its IP.
    print(f"{'Turning ON' if turn_on else 'Turning OFF'} the lamp at {ip_address}!")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()
