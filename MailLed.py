from gpiozero import LED
import smtplib, ssl, getpass, json

def email():
    file = open(r"mail_config.json","r")
    data = json.load(file)
    port = data['port']
    smtp_server = data['smtp']
    sender_email = data['from']
    receiver_email = input("Enter receiver's email address: ")
    password = getpass.getpass("Enter the password: ")
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    
    print("An email was sent")
    file.close()

led = LED(14)

x = input("Enter ON/OFF: ")

if (x.upper() == "ON"):
    led.on()
    message = """\
Subject: LED - Raspberry Pi

The LED is ON"""
else:
    led.off()
    message = """\
Subject: LED - Raspberry Pi

The LED is OFF"""
    
email()