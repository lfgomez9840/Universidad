import socket

HOST = '127.0.0.1'
PORT = 65435

print("Puedes preguntar:")
print("¿Cómo te llamas?")
print("¿Qué hora es?")
print("¿Cuál es la capital de Francia?")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    pregunta = input("Escribe tu pregunta: ")
    s.sendall(pregunta.encode())
    respuesta = s.recv(1024).decode()
    print("Respuesta del servidor:", respuesta)
