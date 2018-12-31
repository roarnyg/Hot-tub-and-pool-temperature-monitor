print("Starting hot tub v1")

import time, machine, onewire, ds18x20

from umqtt.robust import MQTTClient
print("")
print("Hot tub temperature")
print("")

# the device is on GPIO12
dat = machine.Pin(12)

# create the onewire object
ds = ds18x20.DS18X20(onewire.OneWire(dat))

# scan for devices on the bus
roms = ds.scan()
print('found devices:', roms)

# MQTT settings:
myMqttClient = "HOT TUB" #or any other usefull name
adafruitIoUrl = "io.adafruit.com" 
adafruitUsername = "YOUR USERNAME"  
adafruitAioKey = "YOUR UNIQE KEY" 


def connecting():
    try:
        client = MQTTClient(myMqttClient, adafruitIoUrl, 0, adafruitUsername, adafruitAioKey)
        client.connect()
        print("Connected")
        return(client)
        
    except OSError:
        print("Connecting error. Exit")
        finito()
        
def sending(client):
    try:
        ds.convert_temp()
        time.sleep_ms(750)
        print('Temperature:', end=' ')
        
        temp = ds.read_temp(roms[0])
        print(temp)
        client.publish("YOUR USERNAME/feeds/FEEDNAME", str(temp))
        print("Have measured and sent")

    except:
        print("Sending error. Exit")
        time.sleep(0.3)
        client.disconnect()
        finito()

def finito():
    print("Exiting...")
    # configure RTC.ALARM0 to be able to wake the device
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

    # check if the device woke from a deep sleep
    if machine.reset_cause() == machine.DEEPSLEEP_RESET:
            print('Woke from a deep sleep')

    # set RTC.ALARM0 to fire after some milliseconds (waking the device) 
    rtc.alarm(rtc.ALARM0, 140000) #148000 (4min 48 sek: 297000
    time.sleep(2)
    # put the device to sleep
    machine.deepsleep()

client = connecting()
connecting
sending(client)
finito()
