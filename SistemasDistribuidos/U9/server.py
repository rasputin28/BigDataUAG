import socket
import threading
import queue

user_credentials = {}  # A dictionary to store user credentials (username: password)
logged_in_users = {}  # A dictionary to store logged-in users (username: address)
messages = queue.Queue()  # Queue to store received messages
clients = []  # List to keep track of client addresses

# Create a UDP socket for the server
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server on port 9999 at the local address
server.bind(("localhost", 9999))

print('Servidor activo...')

# Function to receive messages from clients
def recv():
    while True:
        try:
            # Receive data from the socket
            message, addr = server.recvfrom(1024)
            messages.put((message, addr))
        except:
            pass

# Function to authenticate a user
def authenticate(username, password):
    return user_credentials.get(username) == password

# Function to transmit messages to clients
def broadcast():
    while True:
        while not messages.empty():
            message, addr = messages.get()
            if addr not in clients:
                clients.append(addr)

            decoded_message = message.decode()
            if decoded_message.startswith("L:"):
                _, username, password = decoded_message.split(":")
                if authenticate(username, password):
                    logged_in_users[username] = addr
                    server.sendto(f"{username} se ha conectado".encode(), addr)
                else:
                    server.sendto("Login fallido: Credenciales incorrectas".encode(), addr)
            elif decoded_message.startswith("R:"):
                _, username, password = decoded_message.split(":")
                if username not in user_credentials:
                    user_credentials[username] = password
                    server.sendto(f"Registro exitoso para {username}".encode(), addr)
                else:
                    server.sendto("Registro fallido: El nombre de usuario ya está en uso.".encode(), addr)
            elif decoded_message.startswith("P:"):
                parts = decoded_message.split(":")
                if len(parts) >= 3:
                    recipient = parts[1]
                    message = ":".join(parts[2:])
                    sender = [user for user, user_addr in logged_in_users.items() if user_addr == addr]
                    if sender and recipient in logged_in_users:
                        server.sendto(f"PRIVATE from {sender[0]}: {message}".encode(), logged_in_users[recipient])
            elif decoded_message.startswith("C:"):
                if addr in logged_in_users.values():
                    sender = [user for user, user_addr in logged_in_users.items() if user_addr == addr]
                    if sender:
                        sender = sender[0]
                        message = ":".join(decoded_message.split(":")[1:])
                        for client in clients:
                            if client != addr:
                                server.sendto(f"C:{sender}:{message}".encode(), client)
                else:
                    server.sendto("No has iniciado sesión. Inicia sesión para chatear.".encode(), addr)

# Create two threads to run the receive and broadcast functions in parallel
t1 = threading.Thread(target=recv)
t2 = threading.Thread(target=broadcast)

# Start the threads
t1.start()
t2.start()
