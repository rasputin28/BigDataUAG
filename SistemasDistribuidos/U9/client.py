import socket
import threading
import random

# Create a UDP socket for the client
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a local IP address and a random port in the range [6000, 7000]
client.bind(("localhost", random.randint(6000, 7000)))

# Function to receive messages from the server
def receive():
    while True:
        try:
            message, _ = client.recvfrom(1024)
            print(message.decode())
        except:
            pass

# Create a thread to execute the receive function in the background
t = threading.Thread(target=receive)
t.start()

print("Escribe 'quit' para salir del chat, 'R:username:password' para registrarte, 'L:username:password' para iniciar sesión, o 'P:recipient_username:message' para enviar un mensaje privado.")
while True:
    message = input()
    if message == "quit":
        client.sendto("quit".encode(), ("localhost", 9999))
        print("Saliendo del chat")
        exit()
    elif message.startswith("R:"):
        # Send a registration request to the server with the format "R:username:password"
        client.sendto(message.encode(), ("localhost", 9999))
    elif message.startswith("L:"):
        # Send a login request to the server with the format "L:username:password"
        client.sendto(message.encode(), ("localhost", 9999))
    elif message.startswith("P:"):
        # Send a private message to a specific user with the format "P:recipient_username:message"
        client.sendto(message.encode(), ("localhost", 9999))
    else:
        # Send a regular chat message to the server with the format "C:message"
        client.sendto(f"C:{message}".encode(), ("localhost", 9999))
