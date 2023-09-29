#!/usr/bin/python
from __future__ import print_function

import hdc20x0


hdc2000 = hdc20x0.Hdc20x0()

print("{ temperature : %3.1f, humidity : %3.1f }" % (hdc2000.readTemperature(), hdc2000.readHumidity()))

