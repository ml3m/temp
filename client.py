import socket

HOST = '127.0.0.1'
PORT = 5005

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    print("Connected to the server!")

    try:
        while True:
            server_message = client_socket.recv(1024).decode()
            print(server_message)

            user_input = input("Enter your input: ").strip()

            client_socket.send(user_input.encode())

            server_response = client_socket.recv(1024).decode()
            print(server_response)

            if user_input.lower() == "exit":
                print("Exiting the game...")
                break

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    start_client()
