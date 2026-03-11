import socket


def echo(connection: socket.socket) -> None | str:
    """Connection handler"""
    while data := connection.recv(1024):
        if data == b'exit\r\n':
            break
        print(f"Полученное сообщение {data}")
        message = b"your message is: " + data
        connection.sendall(message)
    raise Exception

def listen_for_connection(server_socket: socket.socket):
    """Listens for incoming connections"""
    while True:
        try:
            connection, address = server_socket.accept()
            print(f"{address} connected")
            echo(connection)
        except Exception:
            print("Connection closed")
            break
        
