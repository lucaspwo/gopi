import socket, re
from picamera import PiCamera
from time import sleep
from datetime import datetime
import piconv_1080, piconv_720

camera = PiCamera()
# class Grava1080 ():
    # def __init__(self):
    #     threading.Thread.__init__(self)
        # exitFlag = False
        # exitMutex = threading.Lock()
    # def run(self):
        # pass
def Grava1080():
    print('Gravando 1080p')
    camera.rotation = 270
    camera.resolution = (1920, 1080)
    camera.framerate = 30
    data = datetime.now()
    ano = str(data.year)
    mes = checa(data.month)
    dia = checa(data.day)
    hora = checa(data.hour)
    minuto = checa(data.minute)
    segundo = checa(data.second)
    arq = ano+mes+dia+hora+minuto+segundo+'.h264'
    camera.start_recording('/home/pi/Videos/Videos_h264_1080/'+arq)
    return arq
    # while True:
    #     with exitMutex:
    #             if exitFlag:
    #                 break

def Grava720():
    print('Gravando 720p')
    camera.rotation = 270
    camera.resolution = (1280, 720)
    camera.framerate = 60
    data = datetime.now()
    ano = str(data.year)
    mes = checa(data.month)
    dia = checa(data.day)
    hora = checa(data.hour)
    minuto = checa(data.minute)
    segundo = checa(data.second)
    arq = ano+mes+dia+hora+minuto+segundo+'.h264'
    camera.start_recording('/home/pi/Videos/Videos_h264_720/'+arq)
    return arq


# def Para1080():
#     global camera
#     camera.stop_recording()

# def Para720():
#     global camera
#     camera.stop_recording()
    """ Instruct the serial thread to exit."""
    # with exitMutex:
    #     exitFlag = True

def checa(i):
    if(i < 10):
        s = str(0)+str(i)
        return s
    else:
        return str(i)

flag = False
f1080 = False
f720 = False
val1 = ''
val2 = ''
arq1080 = ''
arq720 = ''

pagWeb = open('PagWeb.html').read()
gr1080 = open('gr1080.html').read()
gr720 = open('gr720.html').read()

# thread_Grava1080 = Grava1080()
# thread_Grava1080.start()

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print ('Rodando...')

try:
    while flag == False:
        # print ('Conectou')
        conn, addr = s.accept()
        request = conn.recv(1024)
        if f1080 == False and f720 == False:
            # print(request.decode("utf-8"))
            request = str(request)[3:50]
            m = re.search(r'(gravar=.*p)', request)
            if m is not None:
                val1 = m.group(0)[7:]
                print(val1)
                if val1 == 'Gravar+1080p':
                    f1080 = True
                    conn.send(gr1080.encode())
                    conn.close()
                    sleep(1)
                    arq1080 = Grava1080()
                elif val1 == 'Gravar+720p':
                    f720 = True
                    conn.send(gr720.encode())
                    conn.close()
                    sleep(1)
                    arq720 = Grava720()
            else:
                # flag = True
                conn.send(pagWeb.encode())
                # conn.close()
        elif f1080 == True and f720 == False:
            # print(request.decode("utf-8"))
            request = str(request)[3:50]
            m = re.search(r'(parar=.*p)', request)
            if m is not None:
                val2 = m.group(0)[6:]
                print(val2)
                if val2 == 'Parar+1080p':
                    f1080 = False
                    conn.send(pagWeb.encode())
                    conn.close()
                    sleep(1)
                    camera.stop_recording()
                    # Para1080()
                    piconv_1080.init(arq1080)
            else:
                conn.send(gr1080.encode())
                conn.close()
                sleep(1)
        elif f1080 == False and f720 == True:
            # print(request.decode("utf-8"))
            request = str(request)[3:50]
            m = re.search(r'(parar=.*p)', request)
            if m is not None:
                val2 = m.group(0)[6:]
                print(val2)
                if val2 == 'Parar+720p':
                    f720 = False
                    conn.send(pagWeb.encode())
                    conn.close()
                    sleep(1)
                    camera.stop_recording()
                    # Para720()
                    piconv_720.init(arq720)
            else:
                # print('Aqui?')
                conn.send(gr720.encode())
                conn.close()
                sleep(1)
finally:
    s.close()
    # thread_Grava1080.exit()
