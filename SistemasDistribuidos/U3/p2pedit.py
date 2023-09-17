import socket
import time

ip_amigo = '127.0.0.1'  

port = 12345

# Instanciar socket UDP
node_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
node_socket.bind(('0.0.0.0', port))  # Conectar con todos los puertos disponibles

while True:
    print(f'Este dispositivo esta tratando de conectarse a {ip_amigo}:{port}')
    node_socket.sendto('Hola'.encode('utf-8'), (ip_amigo, port))
    respuesta, direccion = node_socket.recvfrom(1024)
    
    if respuesta.decode('utf-8') == 'Hola':  # Revisar respuesta de confirmacion
        print('Tu amigo esta conectado')
        print('Escribele a tu amigo')
        mensaje = input(str())
        node_socket.sendto(mensaje.encode('utf-8'), (ip_amigo, port))
        respuesta, direccion = node_socket.recvfrom(1024)
        if respuesta.decode('utf-8') == 'salir':
            node_socket.close()
            break
    else:
        print('Tu amigo no esta conectado')
        time.sleep(2)
        print('Esperando unos momentos para ver si se conecta...')
        time.sleep(10)
