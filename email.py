import smtplib

sender = 'pankajkundu9@gmail.com'
receivers = ['pkundu@raintreeinc.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

smtpObj = smtplib.SMTP('smtp.gmail.com',587)
smtpObj.starttls()
smtpObj.login('pankajkundu9@gmail.com','%password%')
smtpObj.sendmail( sender,receivers, message)         
print ("Successfully sent email")