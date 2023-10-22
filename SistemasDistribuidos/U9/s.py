# Nombre: Aridai Solis Sanchez
# UAG ID: 5022636

import socket
import cv2
import pickle
import struct
import imutils

# Crear un socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '127.0.0.1'  # Dirección IP del host al que se conectará (en este caso, localhost)
port = 10050  # Puerto al que se conectará (los puertos no privilegiados son > 1023)

# Conectar al servidor web en el número de puerto especificado
client_socket.connect((host_ip, port))

# Crear variables para recibir y procesar los datos
data = b""
payload_size = struct.calcsize("Q")

while True:
    while len(data) < payload_size:
        packet = client_socket.recv(4 * 1024)
        if not packet:
            break
        data += packet

    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packed_msg_size)[0]

    while len(data) < msg_size:
        data += client_socket.recv(4 * 1024)

    frame_data = data[:msg_size]
    data = data[msg_size:]
    frame = pickle.loads(frame_data)
    cv2.imshow("Recibiendo...", frame)
    key = cv2.waitKey(10)

    if key == 13:
        break

client_socket.close()
