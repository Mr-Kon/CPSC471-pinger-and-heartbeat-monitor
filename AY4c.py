# udp_pingclient
from socket import *
import time

serverName = 'localhost'
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientPort = 12000
i = 1
while True:
	time.sleep(5)
	clientSocket.settimeout(10)
	message = f'heartbeat pulse {i}'
	clientSocket.sendto(message.encode(), (serverName, clientPort))
	try:
		modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
		print(message)
	except timeout:
		break
	i += 1
clientSocket.close()
