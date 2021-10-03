# udp_heartbeat_server
from socket import *
import time
# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
while True:
	serverSocket.settimeout(10)
	try:
		startTime = time.time()
		# Receive the client packet along with the address it is coming from
		message, address = serverSocket.recvfrom(1024)
		totalTime = time.time() - startTime
	except timeout:
		break
	if totalTime > 10:
		break
	print(f'Server received {message.decode()} Pulse interval was {round(totalTime)} seconds')
	# The server responds
	serverSocket.sendto(message, address)

print('No pulse after 10 seconds. Server quits')
print('Server stops.')
serverSocket.close()