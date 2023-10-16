import socket

def send_file(conn, filename):
    try:
        with open(filename, 'rb') as file:
            total_sent = 0
            while True:
                data = file.read(1024)  # Leer 1024 bytes a la vez
                if not data: 
                    break
                conn.send(data)
                total_sent += len(data)
                print(f"Enviando {total_sent} bytes...")
        conn.send(b'DONE')
        print(f"El archivo '{filename}' se envio.")
    except Exception as e:
        print(f"Error al enviar el archivo: {str(e)}")
    finally:
        conn.close()

def main():
    host = '127.0.0.1'  # Direccion IP del servidor
    port = 12345       # Puerto donde se escucha el servidor

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Escuchar una conexion entrante

    print(f"Servidor escuchando en {host}:{port}")

    while True:
        conn, addr = server_socket.accept()  # Aceptar conexiones entrantes
        print(f"Conexion de {addr}")
        
        filename = '/root/UAG/SistemasDistribuidos/U7/ej.mp4'  # Cambia esto al nombre del archivo que quieres enviar
        send_file(conn, filename)

if __name__ == "__main__":
    main()
