import socket
import threading

HOST = '127.0.0.1'
PORT = 65434

def recibir_mensajes(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())
        except:
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Conectado al chat. Escribe tus mensajes y presiona Enter.")
    hilo = threading.Thread(target=recibir_mensajes, args=(s,))
    hilo.daemon = True
    hilo.start()
    while True:
        mensaje = input()
        if mensaje.lower() == "salir":
            break
        s.sendall(mensaje.encode())

