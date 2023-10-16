import socket
import cv2
import pickle
import struct
import imutils

# Create Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_address = ('127.0.0.1', 9999)

# Enlazar el socket
server_socket.bind(socket_address)

# Escuchar
server_socket.listen(5)
print("LISTENING AT:", socket_address)

while True:
    client_socket, addr = server_socket.accept()
    print('Recibiendo conexión desde:', addr)
    if client_socket:
        vid = cv2.VideoCapture(0)

        while vid.isOpened():
            img, frame = vid.read()
            frame = imutils.resize(frame, width=320)
            a = pickle.dumps(frame)
            message = struct.pack("Q", len(a)) + a
            client_socket.sendall(message)

            cv2.imshow('Transmitiendo video', frame)

            # Rompe el loop cuando se presiona la tecla Enter
            if cv2.waitKey(1) == 13 or not client_socket:
                break

        # Cierra la conexión
        vid.release()
        cv2.destroyAllWindows()
        client_socket.close()
