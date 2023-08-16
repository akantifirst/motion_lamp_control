import subprocess
import paho.mqtt.client as mqtt
import logging
import configparser

# Read configuration
config = configparser.ConfigParser()
config.read('sensor_config.ini')

LOG_FILE_PATH = config['DEFAULT']['LOG_FILE_PATH']
MQTT_BROKER = config['MQTT']['BROKER']
MQTT_PORT = int(config['MQTT']['PORT'])

SENSORS = {
    'SENSOR_1': {
        'MAC': config['SENSOR_1']['MAC'],
        'TOPIC': config['SENSOR_1']['TOPIC']
    },
    'SENSOR_2': {
        'MAC': config['SENSOR_2']['MAC'],
        'TOPIC': config['SENSOR_2']['TOPIC']
    }
    # Add more sensors here as needed
}

# Logging setup
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename=LOG_FILE_PATH,
                    filemode='a')

# MQTT client setup
client = mqtt.Client("ARP_Motion_Detector")
client.connect(MQTT_BROKER, MQTT_PORT)

def arp_detected(line):
    for sensor_name, sensor_data in SENSORS.items():
        if sensor_data['MAC'] in line:
            logging.info(f"ARP Request detected from {sensor_name} with MAC: {sensor_data['MAC']}")
            client.publish(sensor_data['TOPIC'], f"Motion Detected by {sensor_name}")
            break
    else:
        logging.debug(f"Received ARP request but not from any target MACs. Line: {line}")

def main():
    cmd = ["tcpdump", "-l", "-i", "eth0", "arp"]
    
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        for line in iter(process.stdout.readline, ''):
            arp_detected(line)

        process.stdout.close()
        process.wait()
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
