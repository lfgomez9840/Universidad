import socket

HOST = '127.0.0.1'
PORT = 8080  # Puerto típico para pruebas HTTP

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor HTTP escuchando en http://{HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Conexión desde {addr}")
            request = conn.recv(1024).decode()
            print("Petición recibida:")
            print(request)
            # Respuesta HTTP simple
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html; charset=utf-8\r\n"
                "\r\n"
                "<html><body><h1>¡Hola desde tu servidor HTTP en Python!</h1></body></html>"
            )
            conn.sendall(response.encode())
