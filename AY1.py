# udp_pingclient
from socket import *
import time
import sys
import getopt

serverName = 'localhost'
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientPort = 12000
pingTimes = []
pings = 10
timeoutTime = 1
timedOutCount = 0

#parses comand line input
arguments = sys.argv[1:]
optionsString = "p:t:"
args, temp = getopt.getopt(arguments, optionsString)
for flags, var in args:
	if flags in "-p":
		pings = int(var)
	elif flags in "-t":
		timeoutTime = int(var)

i = 0
while i < int(pings):
	clientSocket.settimeout(timeoutTime)
	message = f'seq {i+1} {time.asctime()},'
	startTime = time.time()*1000
	clientSocket.sendto(message.encode(), (serverName, clientPort))
	try:
		modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
		pingTimes.append(round(time.time()*1000 - startTime, 2))
		print(f'Ping {i+1}: host {serverAddress[0]} replied: {modifiedMessage.decode()} RTT = {pingTimes[i-timedOutCount]} ms')
	except timeout:
		print(f'Ping {i+1}: Timed out, message was lost')
		timedOutCount += 1
	i += 1
clientSocket.close()

pingTimes.sort()
avgTime = 0
maxTime = pingTimes[len(pingTimes)-1]
minTime = pingTimes[0]
for j in pingTimes:
	avgTime += j
avgTime = avgTime/float(pings)
losses = (timedOutCount/float(pings)) * 100

print(f'Min RTT = {minTime} ms')
print(f'Max RTT = {maxTime} ms')
print(f'Avg RTT = {round(avgTime,2)} ms')
print(f'Packets lost = {losses} %')