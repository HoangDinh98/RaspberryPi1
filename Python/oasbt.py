#!/usr/bin/python

from gpiozero import LED
from signal import pause
import RPi.GPIO as GPIO
import time

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

IR_PIN = 17
LED_PIN = 18
BUZZ_PIN = 27
BTN_PIN = 22
isActive = 0
got_something = 0

GPIO.setmode(GPIO.BCM)
indicator = LED(BUZZ_PIN)
led1 = LED(LED_PIN)
GPIO.setup(IR_PIN, GPIO.IN)
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

count = 1
sendtime = 0
      
def sendmail() :
  print("Send mail")
  fromaddr = "ronglua83@gmail.com"
  toaddr = "dthx98@gmail.com"
  msg = MIMEMultipart()
  msg['From'] = "Raspberry Anti Theft Device"
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

def security(ev=None) :
  global isActive
  global count
  global sendtime
  
  isActive = not isActive
  
  while isActive:
    got_something = GPIO.input(IR_PIN)
    if got_something:
      indicator.off()
      led1.on()
      sendtime += 1
      if sendtime <= 1 :
        sendmail()
      print("{:>3} Got something".format(count))
    else:
      indicator.on()
      led1.off()
      print("{:>3} Nothing detected".format(count))
    count += 1
    time.sleep(0.01)
  
  
def loop():
    GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, callback=security, bouncetime=200)
    while True:
        pass

def destroy():
    GPIO.cleanup()
    
if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        
