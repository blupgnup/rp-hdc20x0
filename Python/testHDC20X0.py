#!/usr/bin/python
from __future__ import print_function

import time
import hdc20x0


hdc20x0 = hdc20x0.Hdc20x0()
print("Sensor initialized")
print("{ temperature : %3.2f, humidity : %3.2f }" % (hdc20x0.readTemperature(), hdc20x0.readHumidity()))

print("Retrievieng a few values for control:")
for i in range(0, 5):
    print("{ temperature : %3.2f, humidity : %3.2f }" % (hdc20x0.readTemperature(), hdc20x0.readHumidity()))
    time.sleep(1)
    
print("Setting heater on")
hdc20x0.turnHeaterOn()

print("Temperature should climb up:")
for i in range(0, 5):
    print("{ temperature : %3.2f, humidity : %3.2f }" % (hdc20x0.readTemperature(), hdc20x0.readHumidity()))
    time.sleep(0.5)
    
print("Setting heater off")
hdc20x0.turnHeaterOff()

print("Temperature should go down:")
for i in range(0, 5):
    print("{ temperature : %3.2f, humidity : %3.2f }" % (hdc20x0.readTemperature(), hdc20x0.readHumidity()))
    time.sleep(0.5)
