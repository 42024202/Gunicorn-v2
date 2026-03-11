import socket
from sock import echo, listen_for_connection
from pathlib import Path


path = Path(__file__)
HOST = '127.0.0.1'
PORT = 8000

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_addres = ("127.0.0.1", 8000)
    server_socket.bind(server_addres)
    print("Сервер запущен")
    print(f"server address: {server_addres}")
    server_socket.listen(1)
    while True:
        try:
            listen_for_connection(server_socket)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
