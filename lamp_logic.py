def handle_motion(sensor, config, current_states):
    # Retrieve related sensor
    related_sensor = config[sensor]['RELATED_SENSOR']
    
    # If the related sensor's lamp is on and the current sensor detects motion
    if current_states.get(related_sensor, False):
        return (related_sensor, False)  # Turn off related sensor's lamp
    
    # By default, turn on the lamp for the current sensor
    return (sensor, True)
