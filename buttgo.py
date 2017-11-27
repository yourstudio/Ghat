from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
button1=16
button2=12
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while(1):
	if GPIO.input(button1)==0:
		print ("Blue Button ONE Green wire GPIO16 Pressed")
		sleep(.1)
	if GPIO.input(button2)==0:
                print ("Blue Button TWO Yellow wire GPIO 12 :")
                sleep(.1)


