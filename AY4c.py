# udp_pingclient
from socket import *
import time

serverName = 'localhost'
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientPort = 12000
i = 1
while True:
	clientSocket.settimeout(1)
	message = f'heartbeat pulse {i}'
	
	clientSocket.sendto(message.encode(), (serverName, clientPort))
	try:
		modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
		print(f'Ping {i+1}: host {serverAddress[0]} replied: {modifiedMessage.decode()}')
	except timeout:
		print(f'Ping {i+1}: Timed out, message was lost')
	i += 1
clientSocket.close()
