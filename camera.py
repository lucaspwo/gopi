import subprocess
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

i=0

try:
    while True:
        input_state = GPIO.input(12)
        if input_state == 0:
            subprocess.call("raspistill -o /home/pi/Pictures/pic"+str(i)+".jpg", shell=True)
            print('Foto tirada')
            i=i+1
            time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
