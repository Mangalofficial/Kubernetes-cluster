#!/usr/bin/python3

import smtplib, ssl

port = 587  # Port for starttls
smtp_server = "smtp.gmail.com"
sender_email = "my@gmail.com"
receiver_email = "your@gmail.com"
password = "PASSWORD"
message = """
Subject: Error Message
This is test ERROR Message.
"""
try:
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
except:
    print("Error occurred")
else:
    print("Successfully Send")
