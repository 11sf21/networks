from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
  print 'Ready to serve pages, dude'
  connectionSocket, addr = serverSocket.accept()
  try:
    message = connectionSocket.recv(1024)
    filename = message.split()[1]
    f = open(filename[1:])
    outputdata = f.read()
    
    httpMsg = 'HTTP/1.1 200 OK\n'
    connectionSocket.send(httpMsg)
    
    for i in range(0, len(outputdata)):
      connectionSocket.send(outputdata[i])
    connectionSocket.close()
  except IOError:
    errorMsg = '404 Not found man, tough'
    connectionSocket.send(errorMsg)
    connectionSocket.close()
