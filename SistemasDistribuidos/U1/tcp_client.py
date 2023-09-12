import socket

ip_address = '127.0.0.1'
port = 12345

# Instanciar socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definir el mensaje para el servidor
print('Escribeme algo')
message = input(str())

