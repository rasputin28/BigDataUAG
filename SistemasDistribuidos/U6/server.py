import socket
from cryptography.fernet import Fernet


# clave secreta real
secret_key = b'4_841sQzbbQviYng6RJyazEczw-4kTXOn-ZbpeZJQQI='

# Direccion IP y puerto del servidor
server_ip = "127.0.0.1"
server_port = 12345

# Instanciar el socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))

print(f"[*] Escuchando en {server_ip}:{server_port}")

# Inicializar el cifrado Fernet con la clave secreta
cipher_suite = Fernet(secret_key)

while True:
    message, client_address = server_socket.recvfrom(1024)
    
    # Decrypt the received message
    decrypted_message = cipher_suite.decrypt(message)
    
    print(f"[{client_address[0]}:{client_address[1]}] {decrypted_message.decode('utf-8')}")

    # Enviar una respuesta al cliente (esto es opcional)
    response = input("Responder: ")
    
    # Encriptar respuesta antes de enviarla
    encrypted_response = cipher_suite.encrypt(response.encode('utf-8'))
    
    server_socket.sendto(encrypted_response, client_address)
