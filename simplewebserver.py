#  Modules imports
from socket import *

def CreateServer():
    # Server socket
    server_socket = socket(AF_INET, SOCK_STREAM)
    try:
        # We are trying here to bind with the specified url 
        server_socket.bind(('localhost', 9000))
        # If url didn't responsed then client will wait a while then try again
        server_socket.listen(5)
        # our Server sit there and list for connect's
        while True:
            (client_socket, address) = server_socket.accept()
            rd = client_socket.recv(5000).decode()
            piece = rd.split("\n")
            if len(piece) > 0:
                print(piece[0])
            data = 'HTTP/1.1 200 OK\r\n'
            data += 'Content-Type: text/html; charset=utf-8\r\n'
            data += '\r\n'
            data += "<html><body>Hello world I am making this web server to test my python skills</body></html>\r\n\r\n"
            client_socket.sendall(data.encode())
            client_socket.shutdown(SHUT_WR)
    except KeyboardInterrupt:
        print("\nShutting down.......\n")
    except Exception as exc:
        print("Error....\n")
        print(exc)



print('Access http://localhost:9000')
CreateServer()