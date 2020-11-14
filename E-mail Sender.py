#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 21:24:57 2020

@author: muhammadzahidi
"""
import smtplib, ssl

port = 465

email = input("Enter your email:")

password = input("Enter your password:")

recipent = input("Enter the email address to send the email to:")

subject = input("What is the subject of the email:")

text = input("Type your email here:\n")

message = "Subject: {}\n\n{}".format(subject, text)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as servers:
    
    servers.login(email, password)
    
    servers.sendmail(email, recipent, message)

