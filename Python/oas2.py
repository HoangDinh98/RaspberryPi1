#!/usr/bin/python

from gpiozero import LED
from signal import pause
import RPi.GPIO as GPIO
import time

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

GPIO.setmode(GPIO.BCM)

BUZZ_PIN = 27
IR_PIN = 17 

indicator = LED(BUZZ_PIN)
GPIO.setup(IR_PIN, GPIO.IN)

count = 1
sendtime = 0

def sendmail() :
  print("Send mail")
  fromaddr = "ronglua83@gmail.com"
  toaddr = "dthx98@gmail.com"
  msg = MIMEMultipart()
  msg['From'] = fromaddr
  msg['To'] = toaddr
  msg['Subject'] = "DANGEROUS!"
 
  body = "YOUR ROOM IS ATTACKED"
  msg.attach(MIMEText(body, 'plain'))
 
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login(fromaddr, "testdev-11&%")
  text = msg.as_string()
  server.sendmail(fromaddr, toaddr, text)
  server.quit()

while True:
  got_something = GPIO.input(IR_PIN)
  if got_something:
    indicator.off()
    sendtime += 1
    if sendtime <= 1 :
      sendmail()
    print("{:>3} Got something".format(count))
  else:
    indicator.on()
    print("{:>3} Nothing detected".format(count))
  count += 1
  time.sleep(0.01)
