from time import sleep
import RPi.GPIO as GPIO
import os
import time
import signal
import scrollphathd
from scrollphathd.fonts import font5x7
GPIO.setmode(GPIO.BOARD)
button1=16
button2=12
button3=18
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3,GPIO.IN,pull_up_down=GPIO.PUD_UP)
count = 1

while(1):
	if GPIO.input(button2)==0:
        if count == 4:
			scrollphathd.clear()
			scrollphathd.show()
			scrollphathd.write_string("four 4 track", x=0, y=0, font=font5x7, brightness=0.5)
			scrollphathd.show()
			print(count)
			count = 0
			sleep(.1)
		if count == 3:
			scrollphathd.clear()
			scrollphathd.show()
			scrollphathd.write_string("three", x=0, y=0, font=font5x7, brightness=0.5)
			scrollphathd.show()
			print(count)
			count += 1
			sleep(.1)
		if count == 2:
			scrollphathd.clear()
			scrollphathd.show()
			scrollphathd.write_string("two", x=0, y=0, font=font5x7, brightness=0.5)
			scrollphathd.show()
			print(count)
			count += 1
			sleep(.1)
		if count == 1:
			scrollphathd.clear()
			scrollphathd.show()
			scrollphathd.write_string("one 1 track ", x=0, y=0, font=font5x7, brightness=0.5)
			scrollphathd.show()
			print(count)
			count += 1
			sleep(.1)
		
		if count == 0:
			count =1
		
		
		print ("buton NEXT:")
		print(count)
		sleep(.1)

	if GPIO.input(button1)==0:

		print("""Scroll pHAT scrolls Press Ctrl+C to exit!""")
		scrollphathd.show()
		scrollphathd.scroll()
		sleep(.01)
		











    
    
