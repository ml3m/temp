import socket
import threading

HOST = '127.0.0.1'
PORT = 5005

def handle_client(connection):
    conn, addr = connection
    print(f"Connected to {addr}")

    try:
        while True:
            conn.send("Welcome to the game! Enter your input:".encode())

            client_message = conn.recv(1024).decode()

    except Exception as e:
        print(f"Error with client {addr}: {e}")
    finally:
        conn.close()
        print(f"Connection with {addr} closed.")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"Server is running on {HOST}:{PORT}")

    while True:
        connection = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(connection,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
