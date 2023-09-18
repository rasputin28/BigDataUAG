import socket
import threading
import queue
import time

'''Este codigo tiene a su disponibilidad un numero amplio de clientes conectados, solo limitados al tamano del intervalo de los puertos de enlace'''

# Cola para almacenar mensajes recibidos de los clientes
messages = queue.Queue()

# Lista para llevar un registro de las direcciones de los clientes conectados
clients = []

# Crear un socket UDP
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enlazar el socket al servidor en el puerto 9999 en la dirección local
server.bind(("localhost", 9999))

print('Servidor activo...')

# Función para recibir mensajes de los clientes
def recv():
    while True:
        try:
            # Recibir datos del socket
            message, addr = server.recvfrom(1024)

            # Colocar el mensaje en la cola junto con la dirección del remitente
            messages.put((message, addr))
        except:
            pass

# Función para transmitir mensajes a los clientes
def broadcast():
    while True:
        while not messages.empty():
            message, addr = messages.get()

            # Si la dirección del remitente no está en la lista de clientes, agréguela
            if addr not in clients:
                clients.append(addr)

            # Enviar el mensaje a todos los clientes
            for client in clients:
                try:
                    # Comprobar si el mensaje comienza con "SIGNUP_TAG:" (etiqueta de registro)
                    if message.decode().startswith("SIGNUP_TAG:"):
                        # Extraer el nombre del cliente del mensaje
                        name = message.decode()[message.decode().index(":")+1:]

                        # Enviar un mensaje de notificación de unión al chat a todos los clientes
                        server.sendto(f"{name} se unió al chat".encode(), client)
                    else:
                        # Enviar el mensaje recibido a todos los clientes
                        server.sendto(message, client)
                except:
                    # Si no se puede enviar el mensaje al cliente, eliminarlo de la lista de clientes
                    clients.remove(client) 

# Crear dos hilos para ejecutar las funciones de recibir y transmitir en paralelo
t1 = threading.Thread(target=recv)
t2 = threading.Thread(target=broadcast)

# Iniciar los hilos
t1.start()
t2.start()
