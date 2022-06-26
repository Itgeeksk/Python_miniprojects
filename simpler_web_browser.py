# import's 

import socket

# Getting url here
url = input("Enter the url here: ")
# opening a socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# calling the connect function of socket to connet the data
mysocket.connect(( "google.com", 80))
# Forming the url 
cmd = f'{url}\r\n\r\n'.encode()
# Sending the request
mysocket.send(cmd)

# Looping to get data in nicer form
while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

# closing the socket
mysocket.close()