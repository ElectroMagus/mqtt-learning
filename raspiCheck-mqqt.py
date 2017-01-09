# MQTT Library Import
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import psutil, datetime

# Generate intial CPU Utilization Counters
psutil.cpu_percent();

# Generate CPU Stats
cpuCount = psutil.cpu_count();
print "CPU Count: ",cpuCount;

# Generate Memory Stats
virtualmemoryStats = psutil.virtual_memory();
totalVM = virtualmemoryStats[0];
availVM = virtualmemoryStats[1];
print "Total Memory: ",totalVM
print "Availible Memory: ",availVM

# Root Parition Space
rootStats = psutil.disk_usage('/')
rootTotal = rootStats[0];
rootUsed = rootStats[1];
rootFree = rootStats[2];
rootPercent = rootStats[3];
print "Root Parition: ",rootTotal," total - ",rootUsed," used - ",rootFree," free - ",rootPercent," % free"

# Determine Uptime
lastBoot = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
print "Last Boot Time/Date: ",lastBoot

# Generating CPU Utilization Usage (Can hang the program)
cpuUtil = psutil.cpu_percent(interval=5, percpu=True)
print "CPU Utilization: ",cpuUtil[0],"% Proc 1   ",cpuUtil[1],"% Proc 2   ",cpuUtil[2],"$ Proc 3   ",cpuUtil[3],"% Proc 4"
#mqttc = mqtt.Client(client_id="chomper")
#mqttc.connect("octokong", 1883)
#mqttc.publish("uptime", uptime())
#mqttc.loop(2)

