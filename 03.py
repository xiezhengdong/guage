#!/home/xiezhengdong/.local/bin/python
import socket
addr=('127.0.0.1',8000)
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(addr)
sock.listen(100)

html='''
HTTP/1.1 200 OK

<html>
<head>
<title>gua</title>
</head>
<body>
<p>%s</p>
</body>
</html>
'''

def get_url(a):
    first_line=a.split('\n')[0]
    url=first_line.split(' ')[1]
    return url
while True:
    print('服务器已经启动')
    cli_sock,cli_addr=sock.accept()
    cli_data=cli_sock.recv(1024).decode('utf8')
    url=get_url(cli_data)
    if url=='/foo':
        b=html%'我有一个非常要好的朋友，我很喜欢和她聊天，和她说话，她就是我最亲爱的老铁，贝贝。哈哈哈哈哈哈哈。'
    elif url=='/bar':
        b=html%'老铁，你要好好加油，好好照顾好自己'
    else:
        b=html%'希望我们可以一直这样，好好的。'
    cli_sock.sendall(b.encode('gbk'))
    cli_sock.close()


