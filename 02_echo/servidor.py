import socket

HOST = '127.0.0.1'
PORT = 65433  # Usa un puerto diferente al anterior

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor Echo escuchando en {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print('Conectado por', addr)
        data = conn.recv(1024)
        print('Mensaje recibido:', data.decode())
        conn.sendall(data)  # Devuelve el mismo mensaje al cliente

