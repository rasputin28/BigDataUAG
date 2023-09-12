import socket

ip_address = '127.0.0.1'
port = 12345

# Instanciar socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establecer conexion
client_socket.connect((ip_address, port))

while True:
    message = input("Escribe un mensaje (o escribe 'salir' para salir): ")
    # Enviar mensaje al servidor
    client_socket.send(message.encode('utf-8'))
    # Recibir respuesta del servidor
    response = client_socket.recv(1024)
    if message == 'salir':
        break

# Enviar mensaje al servidor
client_socket.send(message.encode('utf-8'))

# Recibir respuesta del servidor
response = client_socket.recv(1024)

print(f"Mensaje recibido del servidor: {response.decode('utf-8')}")

# Cerrar el socket
client_socket.close()

