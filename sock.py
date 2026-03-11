import socket


def echo(connection: socket.socket) -> None | str:
    """Connection handler"""
    while data := connection.recv(1024):
        try:
            if data == b'exit\r\n':
                print("Connection closed")
                connection.close()
            print(f"Полученное сообщение {data}")
            message = b"your message is: " + data
            connection.sendall(message)
        except Exception as e:
            print(e)

def listen_for_connection(server_socket: socket.socket) -> None:
    """Listens for incoming connections"""
    try:
        connection, address = server_socket.accept()
        print(f"{address} connected")
        echo(connection)
    except Exception:
        print("Connection closed")
    
