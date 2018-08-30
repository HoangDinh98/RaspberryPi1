import datetime
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def sendmail() :
  print("Sending mail ...")
  fromaddr = "ronglua83@gmail.com"
  toaddr = "dthx98@gmail.com"
  msg = MIMEMultipart()
  msg['From'] = "Raspberry Anti Theft Device"
  msg['To'] = toaddr
  msg['Subject'] = "DANGEROUS [" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "]"
 
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
