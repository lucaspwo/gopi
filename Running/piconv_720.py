import subprocess
# import sys
#import RPi.GPIO as GPIO
#import time
#from datetime import datetime

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(4, GPIO.OUT)

#def checa(i):
#    if(i < 10):
#        s = str(0)+str(i)
#        return s
#    else:
#        return str(i)

#i=0

def init(arq):
#try:
    #while True:
        #input_state = GPIO.input(18)
        #if input_state == 0:
            #GPIO.output(4, GPIO.HIGH)
#data = datetime.now()
#ano = str(data.year)
#mes = checa(data.month)
#dia = checa(data.day)
#hora = checa(data.hour)
#minuto = checa(data.minute)
#segundo = checa(data.second)
    subprocess.call("ffmpeg -r 60 -i /home/pi/Videos/Videos_h264_720/"+arq+" -vcodec copy /home/pi/Videos/Videos_mp4_720/"+arq[:-5]+".mp4", shell=True)
            #print('Foto tirada')
            #GPIO.output(4, GPIO.LOW)
#i=i+1
#time.sleep(0.2)
#except KeyboardInterrupt:
    #GPIO.cleanup()
