#!/usr/bin/python
from __future__ import print_function

import hdc20x0


hdc20x0 = hdc20x0.Hdc20x0()

print("{ temperature : %3.1f, humidity : %3.1f }" % (hdc20x0.readTemperature(), hdc20x0.readHumidity()))

