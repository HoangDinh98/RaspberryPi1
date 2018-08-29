#!/usr/bin/python

from gpiozero import LED
from signal import pause
import threading
import RPi.GPIO as GPIO
import time
import datetime

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

IR_PIN = 17
LED_PIN = 18
BUZZ_PIN = 27
BTN_PIN = 22
isActive = 0
isDurate = 1

priviousTime = datetime.datetime.utcnow()
currentTime = datetime.datetime.utcnow()


GPIO.setmode(GPIO.BCM)
indicator = LED(BUZZ_PIN)
indicator.on()
led1 = LED(LED_PIN)
GPIO.setup(IR_PIN, GPIO.IN)
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

count = 1
sendtime = 0
      
def sendmail() :
  print("Sending mail")
  fromaddr = "ronglua83@gmail.com"
  toaddr = "dthx98@gmail.com"
  msg = MIMEMultipart()
  msg['From'] = "Raspberry Anti Theft Device"
  msg['To'] = toaddr
  msg['Subject'] = "DANGEROUS!"
 
  body = "YOUR ROOM IS ATTACKED"
  msg.attach(MIMEText(body, 'plain'))
 
  try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "testdev-11&%")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("Send mail successfully")
  except:
    print "Can not send Email! Please checking your Network"

def turnOffDivices() :
  indicator.on()
  led1.off()

def setStatus(ev=None) :
  global isActive
  global isDurate
  now = datetime.datetime.now()
  notAvailableTime = (now.minute >= 20 and now.minute <= 21)
  
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
    print "Security is starting in 20 seconds"

def security(ev=None) :
  # global count
  global sendtime
  global priviousTime
  global currentTime
  global isActive
  global isDurate

  if (isDurate) :
    isDurate = 0
    time.sleep(20)
    print "Security is running ..."
  
  while isActive:
    got_something = GPIO.input(IR_PIN)
    if got_something:
      indicator.off()
      led1.on()
      currentTime = datetime.datetime.utcnow()

      isSendMail = (sendtime == 0) or ((currentTime - priviousTime).total_seconds() >= 60)
      
      if isSendMail:
        priviousTime = currentTime
        sendmail()
        sendtime = 1
      # print("{:>3} Got something".format(count))
      
    else:
      indicator.on()
      led1.off()
      # print("{:>3} Nothing detected".format(count))
    # count += 1
    time.sleep(0.01)

def startSecurity() :
  while True:
    security()
  
def loop():
  GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, callback=setStatus, bouncetime=500)
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
        
