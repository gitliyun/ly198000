
from socket import *
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(3)
while True:
    try:
        c,addr = sockfd.accept()
        print('connect from',addr)
    except KeyboardInterrupt:
        print('server exit')
        break
    except Exception as e:
        print(e)
        continue
    while True:
        data = c.recv(1024)
        if not data:
            break
        print("收到：",data.decode())
        c.send(b'chanks')
    c.close()
sockfd.close()