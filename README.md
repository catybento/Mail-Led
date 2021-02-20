# Mail-Led

#### A small python Iot project that sends an email saying the Raspberry Pi LED status

For this project you need:
- Raspberry Pi 2 (Raspberry Pi OS with desktop)
- LED
- 270Ω Resistor

![](Images/IMG_3044.jpg)

To connect the LED, use Raspberry Pi's row of GPIO (General-Purpose Input/Output) like shown in the following picture:
- Ground (14)
- GPIO 14 (8)

![](Images/Raspberry-pi-pinout.jpg)

To run this program, first configure `mail_config.json`:

- "from" - Email address that will send the email
- "smtp" - SMTP address
- "port" - SMTP port

After that, run the program in the **terminal** with the command below:
    
        phyton3 MailLed.py

The terminal should look like this if the program runs properly:

![](Images/IMG_3046.jpg)

You will receive the following email:

![](Images/IMG_3047.PNG)

