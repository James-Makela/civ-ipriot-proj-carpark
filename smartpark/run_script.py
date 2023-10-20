from subprocess import call

call(['sense_emu_gui'])
call(['python', './simple_mqtt_display.py'])
call(['python', './simple_mqtt_sensor.py'])
call(['python', './simple_mqtt_carpark.py'])
