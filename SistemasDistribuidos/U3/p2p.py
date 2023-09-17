import socket
import os
import threading as thread

# Host
HOST = socket.gethostname()

# IP Host
try:
    IP = socket.gethostbyname(HOST)
    print(f'IP del {HOST} es {IP}')
except socket.gaierror as e:
    print("No se pudo resolver el hostname")
    print(e)

IP_HOST = input("Ingresa la IP del host: ")

# Port
PORT = 1234

# IP del receptor
recep = input('Ingresa tu IP: ')

# Crear socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enlace de socket y puerto
s.bind((IP_HOST, PORT))

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

