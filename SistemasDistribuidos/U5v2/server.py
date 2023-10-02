import socket
import threading

# Configuracion del servidor
HOST = '127.0.0.1'
PORT = 12345

# Socket para el servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"El servidor esta escuhando en {HOST}:{PORT}")

# Diccionarios para guardar los jugadores y sus puntajes
players = {}
scores = {}

# Funcion para manejar a los clientes y sus elecciones
def handle_client(client_socket):
    player_name = client_socket.recv(1024).decode()
    players[client_socket] = player_name
    scores[player_name] = 0

    while True:
        try:
            choice = client_socket.recv(1024).decode()
            if not choice:
                break  # Cliente desconectado

            opponent_socket = None
            for sock, name in players.items():
                if sock != client_socket:
                    opponent_socket = sock
                    break

            if opponent_socket:
                opponent_choice = opponent_socket.recv(1024).decode()
                if choice == opponent_choice:
                    result = "Empate"
                elif (
                    (choice == "Piedra" and opponent_choice == "Tijera")
                    or (choice == "Papel" and opponent_choice == "Piedra")
                    or (choice == "Tijera" and opponent_choice == "Papel")
                ):
                    result = f"{player_name} gana!"
                    scores[player_name] += 1
                else:
                    result = f"{players[opponent_socket]} gana!"
                    scores[players[opponent_socket]] += 1

                client_socket.send(result.encode())
                opponent_socket.send(result.encode())

        except ConnectionResetError:
            break
    client_socket.close()
    del players[client_socket]

# Aceptar conexiones de clientes
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Conexion aceptada de {client_address}")
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
