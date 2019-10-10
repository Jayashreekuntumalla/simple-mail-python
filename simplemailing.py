from Lib import smtplib
import ssl

port = 587
smtp_server="smtp.gmail.com"
sender_email="pythontes11@gmail.com"
receiver_email ="pythontes11@gmail.com"
password= input("Type Password here: ")
msg = """\
Subject : Hi There

This message sent from python"""
context = ssl.create_default_context()

with smtplib.SMTP(smtp_server,port) as server:
    server.starttls(context=context)
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,msg)
