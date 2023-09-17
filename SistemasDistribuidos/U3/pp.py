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
        try:
            # Recibir datos 
            data, addr = s.recvfrom(1024)
            message = data.decode('utf-8')

            if message == "salir":
                print("El cliente ha salido")
                break

            print(f"Mensaje recibido de {addr[0]}:{addr[1]}: {message}")
        except Exception as e:
            print("Error al recibir:", e)

def send():
    while True:
        try:
            # Enviar datos 
            msg = input("Mensaje a enviar: ")
            s.sendto(msg.encode('utf-8'), (recep, PORT))

            if msg == "salir":
                print("Saliendo...")
                break
        except Exception as e:
            print("Error al enviar:", e)

# Hilos
envio = thread.Thread(target=send)
recepcion = thread.Thread(target=receive)

# Iniciar hilos
envio.start()
recepcion.start()
