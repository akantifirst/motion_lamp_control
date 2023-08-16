# Motion Lamp Control
The project focuses on automation using simple PIR motion sensors to control lamps. An automation system that uses motion sensors to control lamps in real-time. The system captures ARP requests from motion sensors, publishes them via MQTT, and triggers connected lamps accordingly.

## Features

- Real-time motion detection based lamp control.
- Modular design for easy configuration of multiple sensors and lamps.
- Logic separation allows for quick adjustments to behavior without altering core scripts.

## Getting Started

### Prerequisites

- A Raspberry Pi with the latest version of Raspbian.
- Python 3.x installed.
- Mosquitto (MQTT broker) installed.
- Paho-MQTT Python library.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/motion_lamp_control.git
   cd motion_lamp_control
   ```
2. Install the required Python libraries:
   ```
   pip3 install -r requirements.txt
   ```

### Configuration

1. Update the `lamp_logic_config.ini` with your MQTT broker details, sensors, and lamp IPs.
2. If needed, modify the lamp_logic.py for custom behavior or control logic.

### Running the scripts

1. Start the motion detection script:
   ```
   python3 motion_detector.py
   ```
2. Start the lamp control script:
   ```
   python3 lamp_controller.py
   ```

### Usage

Once both scripts are running, the system will monitor ARP requests from configured motion sensors and control lamps based on the logic provided in lamp_logic.py.

### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
   
