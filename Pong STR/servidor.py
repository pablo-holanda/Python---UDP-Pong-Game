import socket
import thread
import serial
import time

#HOST = socket.gethostbyname(socket.gethostname())
HOST = '127.0.0.1'
print HOST
PORT = 2020	#Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
ser = serial.Serial('/dev/tty.usbmodem1411', 9600)

def lerSerial():
   time.sleep(5)
   while True:
      placar = ser.readline()
      print placar
      udp.sendto(placar,jogador1)
      #udp.sendto(placar,jogador2)

thread.start_new_thread(lerSerial, ())

while True:
   msg, cliente = udp.recvfrom(1024)
   #guardar os Ips dos jogadores
   if msg == "8":
      jogador1 = cliente
   elif msg == "9":
   	jogador2 = cliente
   else:
   	ser.write(msg)

udp.close()


