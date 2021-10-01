# udppingclient_no_loss
from socket import *
import time

serverName = 'localhost'
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientPort = 12000
pingTimes = []
pings = input('How many pings do you want to send: ')
i = 0
while i < int(pings):
	clientSocket.settimeout(1)
	message = f'seq {i+1} {time.asctime()},'
	startTime = time.time()*1000
	clientSocket.sendto(message.encode(), (serverName, clientPort))
	modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
	pingTimes.append(round(time.time()*1000 - startTime, 2))
	print(f'Ping {i+1}: host {serverAddress[0]} replied: {modifiedMessage.decode()} RTT = {pingTimes[i]} ms')
	#print(modifiedMessage.decode())
	i += 1
clientSocket.close()

pingTimes.sort()
avgTime = 0
maxTime = pingTimes[len(pingTimes)-1]
minTime = pingTimes[0]
for j in pingTimes:
	avgTime += j
avgTime = avgTime/float(pings)
print('Minimum RTT:', maxTime, 'ms')
print('Maximum RTT:', minTime, 'ms')
print('Average RTT:', avgTime, 'ms')
