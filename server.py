#!/usr/bin/python3.6
import socket
addr=('127.0.0.1',8000)
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(addr)
sock.listen(100)

html=b'''
HTTP/1.1 200 OK

<html>
<head>
<title>shishaungting</title>
</head>
<body>
<p><strong>hello world</strong></p>
<p>we are family</p>
</body>
</html>
'''

while True:
    print("服务器已经启动")
    cli_sock,cli_addr=sock.accept()
    cli_data=cli_sock.recv(1024)
    print("服务器接受到的报文信息是:\n%s"%cli_data.decode('utf8'))
    cli_sock.sendall(html)
    cli_sock.close()
