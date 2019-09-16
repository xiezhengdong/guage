#!/usr/bin/env python3.6
import socket
addr=('127.0.0.1',8000)
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(addr)
sock.listen(100)

html=b'''
HTTP/1.1 200 OK

<html>
<head>
<title>guage</title>
</head>
<body>
hello
</body>
</html>
'''
while True:
    print('服务器正在连接')
    cli_sock,cli_addr=sock.accept()
    cli_data=cli_sock.recv(1024)
    print('接受到的报文是：\n%s'%cli_data.decode('utf8'))
    cli_sock.sendall(html)
    cli_sock.close()
