# MQTT Library Import
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import socket

mqttc = mqtt.Client()
mqttc.connect("octokong", 1883)
mqttc.publish("system/heartbeat", socket.gethostname(), qos=1, retain=True)
mqttc.loop(2)

