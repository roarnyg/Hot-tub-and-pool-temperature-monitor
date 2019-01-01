# Hot tub and pool temperature monitor

## Make our own, online temperatur monitor. 

With the power of [Micropython](http://micropython.org/) it is easy to measure temperature in your hot tub, swimming pool, living room, garden house etc. The temperature is transfered with MQTT protocol to [https://io.adafruit.com/](io.adafruit.com). You can monitor the temperature on Adafruits web page for free. Of course, you can use any other MQTT broker if you like.

![Circuit board with ESP8266 and resistor](https://raw.githubusercontent.com/roarnyg/hot-tub-and-pool-temperature-monitor/master/Circuit%20board.jpg, height=20)

## Equipment:
* Microcontroller: ESP8266 (NodeMCU, WeMos etc.)
* Temperature sensor: DS18B20
* Solderless breadboard and cables or curcuit board
* 4.7 kOhm resistor 
* USB Powerbank
* Water proof enclosure

The MCU is powered by a USB power bank. 2000mAh power bank works for several days becasue the script shuts down the MCU to deep sleep mode (battery saving) while not measuring and transfering.

The resistor should be connected between 3.3V and the data cable from the temperature sensor. 

You will find more explanation in the micropython script. 
