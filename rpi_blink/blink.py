#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED_PIN=40
GPIO.setup(LED_PIN, GPIO.OUT)
while True:
      GPIO.output(LED_PIN, True)
      time.sleep(2)
      GPIO.output(LED_PIN ,False)
      time.sleep(2)
