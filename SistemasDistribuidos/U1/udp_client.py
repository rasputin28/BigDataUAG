import socket 

# Direccion IP del servidor y puerto
server_ip = "127.0.0.1"
server_port = 12345

# Instanciar el socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Definir el mensaje para el servidor
print('Escribeme algo')
message = input(str())

# Enviar el mensaje al servidor
client_socket.sendto(message.encode('utf-8'), (server_ip, server_port))

# Recibir respuesta del servidor
response, server_address = client_socket.recvfrom(1024)

# Mostrar respuesta del servidor
print(f"La respuesta del servidor: {response.decode('utf-8')}")

# Cerrar el socket
client_socket.close()