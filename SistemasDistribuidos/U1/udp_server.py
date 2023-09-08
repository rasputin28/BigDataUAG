import socket

# Direccion IP del servidor y puerto
server_ip = "127.0.0.1"
server_port = 12345

# Instanciar el socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enlazar el socket a la direccion IP y el puerto
server_socket.bind((server_ip, server_port))

print(f"El servidor UDP esta escuhando en {server_ip}:{server_port}")

while True:
    # Recibir datos del cliente
    data, client_address = server_socket.recvfrom(1024)

    # Mostrar datos recibidos
    print(f"Datos recibidos de {client_address}: {data.decode()}")

    # Enviar una respuesta al cliente
    response = 'Adios cliente UDP'
    server_socket.sendto(response.encode(), client_address)