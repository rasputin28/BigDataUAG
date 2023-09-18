import socket
import threading
import random

# Crear un socket UDP para el cliente
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enlazar el socket a una dirección IP local y un puerto aleatorio en el rango [6000, 7000]
client.bind(("localhost", random.randint(6000, 7000)))

# Solicitar al usuario que ingrese su nombre
name = input("Escribe tu nombre: ")

# Función para recibir mensajes del servidor
def receive():
    while True:
        try:
            # Recibir mensajes del servidor
            message, _ = client.recvfrom(1024)
            # Decodificar y mostrar el mensaje
            print(message.decode())
        except:
            pass

# Crear un hilo para ejecutar la función de recibir en segundo plano
t = threading.Thread(target=receive)
t.start()

# Enviar un mensaje de registro al servidor con el nombre del cliente
client.sendto(f"SIGNUP_TAG:{name}".encode(), ("localhost", 9999))

# Esperar que el usuario ingrese mensajes y enviarlos al servidor
while True:
    message = input()
    if message == "quit":
        # Enviar un mensaje de salida al servidor cuando el usuario quiere salir
        client.sendto(f"{name} salió del chat".encode(), ("localhost", 9999))
        print(f"{name} salió del chat")
        exit()
    else:
        # Enviar el mensaje al servidor con el nombre del cliente
        client.sendto(f"{name}: {message}".encode(), ("localhost", 9999))
