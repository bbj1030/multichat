from socket import socket, SOCK_DGRAM
import json

udp_sk = socket(type=SOCK_DGRAM)
udp_sk.bind(("10.3.88.88", 8082))

username = input("请输入用户名：")

while True:
    menu = '''欢迎来到QQ聊天室
        1. 上线
        2. 下线
        3. 发送会话
        4. 接收会话
        5. 退出'''
    print(menu)

    user_select = int(input("请输入您的选择"))

    if user_select == 1:

        msg = "上线"+":"+username

        udp_sk.sendto(msg.encode("utf-8"), ("10.3.88.88", 9000))

        json_dict1, server_addr = udp_sk.recvfrom(1024)
        dict1 = json.loads(json_dict1.decode("utf-8"))
        print(dict1)



    elif user_select == 2:
        msg = "下线" + ":" + username

        udp_sk.sendto(msg.encode("utf-8"), ("10.3.88.88", 9000))

    elif user_select == 3:
        # 聊天
        p1 = input("请输入聊天对象：")
        p1_addr = tuple(dict1[p1])
        print(p1_addr)

        # 聊天过程
        while True:
            msg = input('请输入消息,回车发送,输入q结束和他的聊天: ').strip()
            if msg == 'q': break
            if not msg: continue
            msg = '发给' + p1 + ': ' + msg
            udp_sk.sendto(msg.encode('utf-8'), p1_addr)  # 必须带着自己的地址，这就是UDP不一样的地方，不需要建立连接，但是要带着自己的地址给服务端，否则服务端无法判断是谁给我发的消息，并且不知道该把消息回复到什么地方，因为我们之间没有建立连接通道

            # back_msg, addr = udp_sk.recvfrom(1024)  # 同样也是阻塞状态，等待接收消息
            # print('来自[%s:%s]的一条消息:\033[1;34;43m%s\033[0m' % (addr[0], addr[1], back_msg.decode('utf-8')))

    elif user_select == 4:
        while True:
            qq_msg, addr = udp_sk.recvfrom(1024)  # 阻塞状态，等待接收消息
            if qq_msg.decode("utf-8") == "发给李四: 88": break
            print('来自[%s:%s]的一条消息:\033[1;34;43m%s\033[0m' % (addr[0], addr[1], qq_msg.decode('utf-8')))
            # back_msg = input('回复消息: ').strip()
            #
            # udp_sk.sendto(back_msg.encode('utf-8'), addr)

    elif user_select == 5:
        break
    else:
        print("请输入正确选择")
