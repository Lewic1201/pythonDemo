from socket import *
from threading import Thread


def talk(conn):
    while True:
        try:
            data = conn.recv(1204)
            if not data:
                break
            conn.send(data.upper())
        except ConnectionResetError:
            break
        finally:
            conn.close()


def server(ip, port):
    server_socket = socket(AF_INET, SOCK_STREAM)

    server_socket.bind((ip, port))
    server_socket.listen(1)

    while True:
        conn, addr = server_socket.accept()
        try:
            p = Thread(target=talk, args=(conn,))
            p.start()
        finally:
            conn.close()


if __name__ == '__main__':
    server('127.0.0.1', 8081)
