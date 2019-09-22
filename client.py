import socket

# ip_port = ('127.0.0.1', 9)
ip_port = ('39.96.177.143', 5000)
s = socket.socket()
s.connect(ip_port)

while True:

    send_data = input(">>: ").strip()
    if len(send_data) == 0:
        continue

    s.send(bytes(send_data, encoding='utf8'))

    if send_data == 'exit':
        break

    recv_data = s.recv(1024)
    print(str(recv_data, encoding='utf8'))

s.close()
