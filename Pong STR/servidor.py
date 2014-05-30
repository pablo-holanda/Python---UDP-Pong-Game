import socket
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

while True:
   msg, cliente = udp.recvfrom(1024)
   #print cliente, msg
   mensagem = msg.split() # Cria uma lista mensagem com os termos da str msg
   jogador = mensagem[0]
   sentido = mensagem[1]
   print('Jogador: {}'.format(jogador) + ('  -  ') + ('Sentido: {}'.format(sentido)))
udp.close()