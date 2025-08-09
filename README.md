# Taller 1 - Arquitectura de Software: Cliente-Servidor

Este repositorio contiene la solución al Taller 1 de Arquitectura de Software, donde se exploran diferentes modelos de comunicación cliente-servidor usando Python y sockets.  
**Autor:** Luis Felipe Gomez  
**Universidad:** Corporación Universitaria Remington  
**Materia:** Arquitectura de Software

## Estructura del Proyecto

as-taller1/
├── 01sockets/
│ ├── cliente.py
│ └── servidor.py
├── 02echo/
│ ├── cliente.py
│ └── servidor.py
├── 03chat/
│ ├── cliente.py
│ └── servidor.py
├── 04http/
│ └── servidor.py
├── 05proyecto/
│ ├── cliente.py
│ └── servidor.py
├── requirements.txt
├── README.md
└── .gitignore


## Ejercicios

### 1. Sockets Básicos (`01_sockets/`)

- **Descripción:** Comunicación simple entre un cliente y un servidor. El cliente envía un mensaje y el servidor lo recibe.
- **¿Cómo probar?**
  1. Ejecuta el servidor: `python3 01_sockets/servidor.py`
  2. Ejecuta el cliente: `python3 01_sockets/cliente.py`

---

### 2. Servidor Echo (`02_echo/`)

- **Descripción:** El servidor recibe un mensaje y lo devuelve al cliente (eco).
- **¿Cómo probar?**
  1. Ejecuta el servidor: `python3 02_echo/servidor.py`
  2. Ejecuta el cliente: `python3 02_echo/cliente.py`

---

### 3. Chat Multiusuario (`03_chat/`)

- **Descripción:** Varios clientes pueden conectarse y enviarse mensajes entre sí a través del servidor.
- **¿Cómo probar?**
  1. Ejecuta el servidor: `python3 03_chat/servidor.py`
  2. Ejecuta varios clientes en diferentes terminales: `python3 03_chat/cliente.py`

---

### 4. Servidor HTTP Básico (`04_http/`)

- **Descripción:** Un servidor HTTP simple que responde a peticiones desde el navegador.
- **¿Cómo probar?**
  1. Ejecuta el servidor: `python3 04_http/servidor.py`
  2. Abre tu navegador y visita [http://127.0.0.1:8080](http://127.0.0.1:8080)

---

### 5. Proyecto del Estudiante (`05_proyecto/`)

- **Descripción:** Servidor de preguntas y respuestas. El cliente envía una pregunta y el servidor responde si la conoce.
- **¿Cómo probar?**
  1. Ejecuta el servidor: `python3 05_proyecto/servidor.py`
  2. Ejecuta el cliente: `python3 05_proyecto/cliente.py`
  3. Escribe una de las preguntas sugeridas o prueba con otras.

---

## Requisitos

- Python 3.x
- Instalar dependencias (si las hay) con:
  ```bash
  pip install -r requirements.txt

---
