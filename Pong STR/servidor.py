import socket
#import serial

#HOST = socket.gethostbyname(socket.gethostname())
HOST = '127.0.0.1'
PORT = 2020	#Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

#ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
   msg, cliente = udp.recvfrom(1024)
   #print cliente, msg
   #mensagem = msg.split() # Cria uma lista mensagem com os termos da str msg
   #jogador = mensagem[0]
   #sentido = mensagem[1]
   #print('Jogador: {}'.format(jogador) + ('  -  ') + ('Sentido: {}'.format(sentido)))
   ser.write(msg)
   #print msg
   #udp.sendto("10", cliente)
udp.close()
