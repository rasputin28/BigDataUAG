import socket
from cryptography.fernet import Fernet

# clave secreta real
secret_key = b'4_841sQzbbQviYng6RJyazEczw-4kTXOn-ZbpeZJQQI='

# Direccion IP del servidor y puerto
server_ip = "127.0.0.1"
server_port = 12345

# Instanciar el socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Inicializar el cifrado Fernet con la clave secreta
cipher_suite = Fernet(secret_key)

while True:
    # Solicitar al usuario que ingrese un mensaje
    message = input("Escribeme algo: ")
    
    # Encriptar el mensaje antes de enviarlo
    encrypted_message = cipher_suite.encrypt(message.encode('utf-8'))

    # Enviar el mensaje al servidor
    client_socket.sendto(encrypted_message, (server_ip, server_port))

    # Recibir respuesta del servidor
    response, server_address = client_socket.recvfrom(1024)
    
    # Desencriptar respuesta
    decrypted_response = cipher_suite.decrypt(response)

    # Mostrar respuesta del servidor
    print(f"La respuesta del servidor: {decrypted_response.decode('utf-8')}")
