import socket
import threading as thread

# Listar IPs de nodos
print('Lista de IPs de nodos: MAC=192.168.1.64, PC=172.26.103.50')

IP_HOST = input("Ingresa tu IP: ")

# Port
PORT = 12345

# IP del receptor
recep = input('Ingresa la IP del receptor: ')

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
            socket.close()

        print("Mensaje recibido: ", data[0].decode('utf-8'))

def send():
    while True:
        # Enviar datos 
        msg = input("Mensaje a enviar: ")
        s.sendto(msg.encode('utf-8'), (recep, PORT))
        if msg == "salir":
            print("Saliendo...")
            socket.close()

# Hilos
envio = thread.Thread(target=send)
recepcion = thread.Thread(target=receive)

# Iniciar hilos
envio.start()
recepcion.start()

