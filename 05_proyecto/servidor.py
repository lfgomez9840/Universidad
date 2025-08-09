import socket

HOST = '127.0.0.1'
PORT = 65435

respuestas = {
    "¿Cómo te llamas?": "Soy el servidor.",
    "¿Qué hora es?": "No tengo reloj, ¡pero soy rápido!",
    "¿Cuál es la capital de Francia?": "París.",
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor de preguntas escuchando en {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Conexión desde {addr}")
            pregunta = conn.recv(1024).decode()
            print("Pregunta recibida:", pregunta)
            pregunta_normalizada = pregunta.strip().lower()
            respuestas_normalizadas = {k.lower(): v for k, v in respuestas.items()}
            respuesta = respuestas_normalizadas.get(pregunta_normalizada, "No sé la respuesta a eso.")
            conn.sendall(respuesta.encode())
