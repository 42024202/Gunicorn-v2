import socket


HOST = '127.0.0.1'
PORT = 8000

def echo(connection: socket.socket) -> None:
    while data := connection.recv(1024):
        connection.sendall(data)

def listen_for_connection(server_socket: socket.socket):
    while True:
        connection, address = server_socket.accept()
        print(f"{address} connected")
        echo(connection)


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_addres = ("127.0.0.1", 8000)
    server_socket.bind(server_addres)
    print("Сервер запущен")
    print(f"server address: {server_addres}")
    server_socket.listen(1)
    listen_for_connection(server_socket)


if __name__ == "__main__":
    main()
