import socket
import tkinter as tk
from tkinter import messagebox
import threading

# Configuracion del cliente
HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Crear GUI
root = tk.Tk()
root.title("Piedra, papel o tijera")

# Inicializar diccionario para guardar las elecciones de los jugadores
choices = {}

# Funcion para enviar la eleccion del jugador al servidor
def make_choice(choice):
    if len(choices) == 2:
        messagebox.showinfo("Game Over", "Ambos jugadores han hecho su eleccion")
    else:
        client_socket.send(choice.encode())

# Funcion para reiniciar el juego
def reset_game():
    global choices
    choices = {}
    score_label.config(text="Jugador 1: 0 - Jugador 2: 0")

# Elementos de la GUI
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Escoge tu arma:")
label.grid(row=0, column=0, columnspan=3)

rock_button = tk.Button(frame, text="Piedra", width=10, command=lambda: make_choice("Piedra"))
paper_button = tk.Button(frame, text="Papel", width=10, command=lambda: make_choice("Papel"))
scissors_button = tk.Button(frame, text="Tijera", width=10, command=lambda: make_choice("Tijera"))

rock_button.grid(row=1, column=0)
paper_button.grid(row=1, column=1)
scissors_button.grid(row=1, column=2)

# Crear etiqueta para mostrar los puntajes
score_label = tk.Label(frame, text="Jugador 1: 0 - Jugador 2: 0")
score_label.grid(row=2, column=0, columnspan=3)

# Crear boton de reset
reset_button = tk.Button(frame, text="Reiniciar", width=20, command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

# Funcion para actualizar los puntajes
def update_scores(result):
    score_label.config(text=result)

# Funcion para recibir respuestas del servidor
def receive_server_responses():
    while True:
        try:
            server_response = client_socket.recv(1024).decode()
            if not server_response:
                break
            update_scores(server_response)
        except ConnectionResetError:
            break

# Iniciar el thread para recibir respuestas del servidor
response_thread = threading.Thread(target=receive_server_responses)
response_thread.daemon = True
response_thread.start()

root.mainloop()
