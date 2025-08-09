import socket
import threading

HOST = '127.0.0.1'
PORT = 65434

clientes = []

def manejar_cliente(conn, addr):
    print(f"Nuevo cliente conectado: {addr}")
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            mensaje = data.decode()
            print(f"{addr}: {mensaje}")
            # Reenviar el mensaje a todos los clientes conectados
            for c in clientes:
                if c != conn:
                    c.sendall(f"{addr}: {mensaje}".encode())
        except:
            break
    print(f"Cliente desconectado: {addr}")
    clientes.remove(conn)
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor de chat escuchando en {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        clientes.append(conn)
        hilo = threading.Thread(target=manejar_cliente, args=(conn, addr))
        hilo.start()

