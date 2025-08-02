import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor escuchando en {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print('Conectado por', addr)
        data = conn.recv(1024)
        print('Mensaje recibido:', data.decode())
