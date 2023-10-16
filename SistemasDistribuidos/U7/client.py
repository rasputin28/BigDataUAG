import socket

def receive_file(conn, filename):
    try:
        with open(filename, 'wb') as file:
            total_received = 0
            while True:
                data = conn.recv(1024)  # Recibir 1024 bytes a la vez
                if data == b'DONE':
                    print(f"El archivo '{filename}' fue recibido.")
                    break
                file.write(data)
                total_received += len(data)
                print(f"Recibiendo {total_received} bytes...")
    except Exception as e:
        print(f"Error al recibir el archivo: {str(e)}")
    finally:
        conn.close()

def main():
    host = '127.0.0.1'  # Dirección IP del servidor
    port = 12345       # Puerto donde se escucha el servidor

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    filename = 'ej.mp4'  # Cambia esto al nombre del archivo que quieres escribir
    receive_file(client_socket, filename)

if __name__ == "__main__":
    main()
