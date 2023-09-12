import socket

ip_address = '127.0.0.1'
port = 12345

# Instanciar socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establecer conexion del socket a la direccion
server_socket.bind((ip_address, port))

# Escuchar en el puerto
server_socket.listen()

print(f"El servidor esta escuchando en {ip_address}:{port}")

# Aceptar conexiones entrantes
client_socket, client_address = server_socket.accept()

print(f"Conectado por {client_address}")

while True:
    # Recibir datos del cliente
    data = client_socket.recv(1024)
    if not data:
        break # Se cierra si no recibe los paquetes

    print(f"Recibido del cliente {data.decode('utf-8')}")

    # Responde al cliente
    response = 'Mensaje recibido'
    client_socket.send(response.encode('utf-8'))

# Cerrar el socket del cliente
client_socket.close()

# Cerrar el socket del servidor
server_socket.close()

