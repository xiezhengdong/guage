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
<body>%s</body>
</html>
'''
def get_url(request):
    first_line=request.split('\n')[0]
    url=first_line.split(' ')[1]
    return url
while True:
    print('服务器已经启动')
    cli_sock,cli_addr=sock.accept()
    cli_data=cli_sock.recv(1024).decode('utf8')
    print('接受到的报文信息是:%s'%cli_data)
    url=get_url(cli_data)
    if url=='/foo':
        response = html %'我喜欢你，杨子玥'
    elif url=='/bar':
        response = html %'I LOVE YOU 杨子玥'
    else:
        response = html %'hello world'
    print(url,response)
    cli_sock.sendall(response.encode('gbk'))
    cli_sock.close()
    print('连接断开，已经退出')


