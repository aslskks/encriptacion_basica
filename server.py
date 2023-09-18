from socket import socket

# Función para manejar la conexión del servidor
def manejar_conexion_servidor():
    # Definimos la dirección y puerto, la dirección 0.0.0.0 hace referencia a que aceptamos conexiones de cualquier interfaz
    server_address = ('0.0.0.0', 5000)

    # Creamos el socket (la conexión)
    server_socket = socket()

    # Le pasamos la tupla donde especificamos dónde escuchar
    server_socket.bind(server_address)

    # Cantidad de clientes máximos que se pueden conectar
    server_socket.listen(1)

    print("Esperando conexión...")

    # Esperamos a recibir una conexión y aceptarla:
    client_socket, client_address = server_socket.accept()
    print(f"Conexión entrante de {client_address}")

    # Aquí puedes agregar la lógica adicional para manejar la conexión
    try:
        while True:
            # Recibimos datos del cliente (en este caso, asumimos que el cliente envía la clave)
            clave = client_socket.recv(1024).decode()
            if not clave:
                break  # Si no se reciben datos, salimos del bucle

            # Guardamos la clave en el archivo log.txt
            with open('log.txt', 'a') as log_file:
                log_file.write(f"Clave recibida: {clave}\n")

            # Puedes agregar más lógica aquí para manejar los datos según tus necesidades
    except Exception as e:
        print("Error:", str(e))

    # Cerramos la conexión
    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    manejar_conexion_servidor()
