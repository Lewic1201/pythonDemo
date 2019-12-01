from socket import *

ip = '127.0.0.1'
port = 8081

c = socket(AF_INET, SOCK_STREAM)
c.connect((ip, port))

while True:
    msg = input("请输入客户端的信息").strip()
    if not msg:
        continue

    c.send(msg.encode('utf-8'))
    data = c.recv(1024)
    print("收到的信息:", data.decode('utf-8'))
