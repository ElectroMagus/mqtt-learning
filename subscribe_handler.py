# MQTT Library Import
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

## Define Event Callbacks
# CONNACK
def on_connect(mqttc, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    mqttc.subscribe("system/#")

# PUBLISH
def on_message(mqttc, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


# Create client object and setup callbacks 
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

# Conect to server
print "Connecting to server..."
mqttc.connect("octokong", 1883)
# Blocking call loop (check other availible functions for threaded)
mqttc.loop_forever()



