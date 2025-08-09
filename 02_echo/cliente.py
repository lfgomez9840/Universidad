import socket

HOST = '127.0.0.1'
PORT = 65433  # El mismo puerto que el servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    mensaje = "¡Hola, servidor echo!"
    s.sendall(mensaje.encode())
    data = s.recv(1024)
    print("Respuesta del servidor:", data.decode())

