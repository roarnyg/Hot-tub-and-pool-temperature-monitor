# hot-tub-and-pool-monitor
Micropython and MQTT

Equipment:
Microcontroller: ESP8266 (NodeMCU, WeMos etc.)
Temperature sensor: DS18B20
Solderless breadboard and cables or curcuit board
4.7 kOhm resistor 
USB Powerbank
Water proof enclosure

This project uses an ESP8266 and a waterproof temperature sensor, DS18B20 to measure temperature in your hot tub, swimming pool, living room, garden house etc. The temperature is transfered with MQTT protocol to Adafruit.io. You can monitor the temperature on Adafruits web page for free. Of course, you can use any MQTT broker if you like.

The MCU is powered by a USB power bank. 2000mAh power bank works for several days becasue the script shuts down the MCU to deep sleep mode (battery saving) while not measuring and transfering.

The resistor should be connected between 3.3V and the data cable from the temperature sensor. 

You will find more explanation in the micropython script. 
