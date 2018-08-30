#!/usr/bin/python

from gpiozero import LED, Buzzer
from signal import pause
import threading
import RPi.GPIO as GPIO
import time
import datetime

import config as CF
import mail

isActive = 0
isDurate = 0
priviousTime = datetime.datetime.utcnow()
currentTime = datetime.datetime.utcnow()
sendtime = 0

GPIO.setmode( GPIO.BCM )
buzzer = Buzzer( CF.BUZZ_PIN )
buzzer.on()
led = LED( CF.LED_PIN )
GPIO.setup( CF.IR_PIN, GPIO.IN )
GPIO.setup( CF.BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP )

def turnOffDivices() :
  buzzer.on()
  led.off()

def setStatus(ev=None) :
  global isActive
  global isDurate
  now = datetime.datetime.now()
  notAvailableTime = (now.minute >= CF.endEffectTime and now.minute <= CF.startEffectTime)
  
  offAnyWay = isActive or notAvailableTime
  if offAnyWay :
    isActive = 0
    isDurate = 0
    turnOffDivices()
    if notAvailableTime :
      print "Security is not available at this time"
    else:
      print "Security is stopped"
      
  else :
    isActive = 1
    isDurate = 1
    print "Security is starting in", CF.durationTime ,"seconds"

def security(ev=None) :
  global sendtime
  global priviousTime
  global currentTime
  global isActive
  global isDurate

  if (isDurate) :
    isDurate = 0
    time.sleep( CF.durationTime )
    print "Security is running ..."
  
  while isActive:
    got_something = GPIO.input( CF.IR_PIN )
    if got_something:
      buzzer.off()
      led.on()
      currentTime = datetime.datetime.utcnow()

      isSendMail = (sendtime == 0) or ((currentTime - priviousTime).total_seconds() >= CF.sendMailCycle)
      if isSendMail:
        priviousTime = currentTime
        mail.sendmail()
        sendtime = 1
        print "Security is running ..."
      else :
        time.sleep(2)
      
    else:
      buzzer.on()
      led.off()
    time.sleep(0.01)

def startSecurity() :
  while True:
    security()
    time.sleep(0.05)
  
def loop():
  GPIO.add_event_detect( CF.BTN_PIN, GPIO.FALLING, callback=setStatus, bouncetime=500)
  timer = threading.Thread(target = startSecurity)
  timer.daemon = True
  timer.start()
    
if __name__ == '__main__':
  x = False
  try:
    loop()
    while not x: time.sleep(0.1)
  except KeyboardInterrupt:
    exit(1)
        
