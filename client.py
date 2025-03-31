import socket

HOST = '127.0.0.1'
PORT = 5005

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    print("Connected to the server!")

    server_message = client_socket.recv(1024).decode()
    print(server_message)

    try:
        while True:



            if user_input.lower() == "exit":
                print("Exiting the game...")
                break

    except Exception as e:
        print(f"An error occurred: {e}")

    client_socket.close()
    print("Connection closed.")

if __name__ == "__main__":
    start_client()
