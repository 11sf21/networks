from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print "The server is ready to receive"

while True:
  message, clientAddress = serverSocket.recvfrom(2048)
  modifiedMessage = message.upper()
  print "Msg from %s:%d" % (clientAddress[0],clientAddress[1])
  print message
  serverSocket.sendto(modifiedMessage, clientAddress)
