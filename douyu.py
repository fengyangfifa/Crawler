# 爬取斗鱼弹幕

import time
import socket
import multiprocessing
import re
import signal

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET 用于 Internet 进程间通信
# socket.SOCK_STREAM SOCKET_STREAM（流式套接字，主要用于 TCP 协议）或者SOCKET_DGRAM（数据报套接字，主要用于 UDP 协议
host = socket.gethostbyname('openbarrage.douyutv.com')
port = 8601
client.connect((host, port))
# 连接斗鱼弹幕服务器

# 弹幕正则表达式
name_re = re.compile(b'nn@=(.*?)/txt@')
document_re = re.compile(b'txt@=(.*?)/cid@')
# 因为返回的数据是bytes,所以b''

def send_msg(msg):
    '''构造并发送符合斗鱼api的请求'''

    msg = msg.encode('utf-8')
    data_length = len(msg) + 8
    # 8 --> 头部长度
    code = 689
    # 获取客户端传输到服务器格式的数据

    msgHead = int.to_bytes(data_length, 4, 'little') \
        + int.to_bytes(data_length, 4, 'little') \
        + int.to_bytes(code, 4, 'little')
    client.send(msgHead)
    # 发送头
    client.send(msg)
    # 发送数据

def DY_start(id):
    # 构造登录授权请求
    msg1 = 'type@=loginreq/roomid@={}/\0'.format(id)
    send_msg(msg1)
    # 构造获取弹幕消息请求
    msg2 = 'type@=joingroup/rid@={}/gid@=-9999/\0'.format(id)
    send_msg(msg2)

    while True:
        # 服务端返回的数据, 每次最大接受1024个字节
        data = client.recv(1024)
        username = name_re.findall(data)
        document = document_re.findall(data)
        if not data:
            break
        else:
            for i in range(0, len(username)):
                try:
                    print('{}: {}'.format(username[i].decode('utf-8'), document[i].decode('utf-8')))
                except:
                    continue

def logout():
    # 断开与斗鱼服务器的连接
    msg = 'type@=logout//\0'
    send_msg(msg)
    print('已经退出服务器')

def keeplive():
    '''每15秒发送一次心跳包, 告诉服务器自己还在运行'''

    while True:
        msg = 'type@keeplive/tick@={}/\0'.format(int(time.time()))
        send_msg(msg)
        print('发送心跳包')
        time.sleep(15)

def signal_handler(signal, frame):
    '''
    捕捉 ctrl+c的信号 即 signal.SIGINT
    触发hander：
    登出斗鱼服务器
    关闭进程
    '''

    p1.terminate()
    p2.terminate()
    logout()
    print('Bye')


if __name__ == '__main__':
    # 房间号
    room_id = 220185
    # 开启signal捕捉
    signal.signal(signal.SIGINT, signal_handler)

    p1 = multiprocessing.Process(target=DY_start, args=(room_id, ))
    p2 = multiprocessing.Process(target=keeplive)

    p1.start()
    p2.start()