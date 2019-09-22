import socket
ip_port = ('0.0.0.00', 5000)

s = socket.socket()
s.bind(ip_port)
s.listen(5)

while True:

    conn, addr = s.accept()

    while True:

        try:

            recv_data = conn.recv(1024)
            if len(recv_data) == 0:
                break

            send_data = recv_data.upper()
            print(send_data)

            conn.send(send_data)

        except Exception:
            break

    conn.close()
