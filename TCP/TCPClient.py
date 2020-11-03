from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence:')
clientSocket.send(bytes(sentence, encoding='utf8'))
modifiedMessage, serverAddress = clientSocket.recv(1024)
print('From Server: ' + modifiedMessage)
clientSocket.close()
