# udp_heartbeat_server
from socket import *
import time
# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
while True:
	startTime = time.time()
	# Receive the client packet along with the address it is coming from
	message, address = serverSocket.recvfrom(1024)
	totalTime = time.time() - startTime
	if totalTime > 10:
		break
	print(f'Server received {message.decode()} Pulse interval was {totalTime} seconds')
	# The server responds
	serverSocket.sendto(message, address)

print('“No pulse after 10 seconds. Server quits')
serverSocket.close()