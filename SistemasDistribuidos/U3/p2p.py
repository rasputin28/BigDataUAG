import socket
import os
import threading as thread

# Host
HOST = socket.gethostname()

# IP Host
IP = socket.gethostbyname(HOST)
print("IP Host: ", IP)

# Port
PORT = 1234

# IP del receptor
recep = input('Ingresa tu IP: ')

# Crear socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enlace de socket y puerto
s.bind((recep, PORT))

def receive():
    while True:
        # Recibir datos 
        data = s.recvfrom(1024)
        if data[0].decode('utf-8') == "salir":
            print("El cliente ha salido")
            os.exit()

        print("Mensaje recibido: ", data[0].decode('utf-8'))

def send():
    while True:
        # Enviar datos 
        msg = input("Mensaje a enviar: ")
        s.sendto(msg.encode('utf-8'), (recep, PORT))
        if msg == "salir":
            print("Saliendo...")
            os.exit(1)

# Hilos
envio = thread.Thread(target=send)
recepcion = thread.Thread(target=receive)

# Iniciar hilos
envio.start()
recepcion.start()

