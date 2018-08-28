#!/usr/bin/python

from gpiozero import LED
from signal import pause
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_PIN = 27
IR_PIN = 17 

indicator = LED(LED_PIN)
GPIO.setup(IR_PIN, GPIO.IN)

count = 1

while True:
  got_something = GPIO.input(IR_PIN)
  if got_something:
    indicator.on()
    print("{:>3} Got something".format(count))
  else:
    indicator.off()
    print("{:>3} Nothing detected".format(count))
  count += 1
  time.sleep(0.01)
