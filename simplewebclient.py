\
# Importing modules which i need in this script
from socket import *

# Making a  window to call for
mysocket = socket(AF_INET, SOCK_STREAM)
# calling the connecting function
mysocket.connect(('127.0.0.1',9000))
# Forming url
cmd = 'GET http://127.0.0.1:9000/ HTTP/1.0\r\n\r\n'.encode()
mysocket.send(cmd)

# Receving the data
while True:
    data = mysocket.recv(512)
    if len(data)< 1:
        break
    print(data.decode(), end='')


# Closing the connection
mysocket.close()