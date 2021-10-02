# udppingserver_with_delay_and_loss.py
from socket import *
import random
import time
# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
while True:
	# Receive the client packet along with the address it is coming from
	message, address = serverSocket.recvfrom(1024)
	randDellay = random.randrange(10,40)/1000
	time.sleep(randDellay)
	lossChance = random.randrange(1,100)
	if lossChance > 20:
		# The server responds
		serverSocket.sendto(message, address)