import socket
import time

#print('Define la ip de tu amigo')
#ip_amigo = input(str())
ip_amigo = '127.0.0.0'
#print('Define el puerto de comunicacion')
#port = input(int())
port = 12345

# Instanciar socket UDP
node_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Conexion constante
    node_socket.bind((ip_amigo, port))
    print(f'Este dispositivo esta tratando de conectarse a {ip_amigo}:{port}')
    # Mensaje y respuesta de confirmacion
    node_socket.sendto('Hola'.encode('utf-8'), (ip_amigo, port))
    respuesta, direccion = node_socket.recvfrom(1024)
    time.sleep(10)
    if respuesta == True:
        print('Tu amigo esta conectado')
        print('Escribele a tu amigo')
        mensaje = input(str())
        node_socket.sendto(mensaje.encode('utf-8'), (ip_amigo, port))
        respuesta, direccion = node_socket.recvfrom(1024)
        if respuesta == 'salir':
            node_socket.close()
    else:
        print('Tu amigo no esta conectado')
        time.sleep(2)
        print('Esperando unos momentos para ver si se conecta...')
        time.sleep(10)
        # Mandamos otro mensaje de confirmacion por ultima vez
        node_socket.sendto('Hola'.encode('utf-8'), (ip_amigo, port))
        respuesta, direccion = node_socket.recvfrom(1024)
        if respuesta == True:
            print('Tu amigo esta conectado')
        else:
            print('Tu amigo no esta conectado y cerraremos la conexion')
            time.sleep(2)
            print('Adios')
            node_socket.close()
   



    
   
    



