from socket import socket, SOCK_DGRAM
import json
udp_sk = socket(type=SOCK_DGRAM)
udp_sk.bind(("192.168.123.69", 8888))

dict1 = {}


while True:
    try:
        msg, client_addr = udp_sk.recvfrom(1024)
        choose = msg.decode("utf-8").split(":")[0]
        username = msg.decode("utf-8").split(":")[1]
        if choose == "上线":
            dict1[username] = client_addr
            json_dict1 = json.dumps(dict1)
            udp_sk.sendto(json_dict1.encode("utf-8"), client_addr)

            print('\033[1;34;43m用户%s已上线\033[0m' % username)

        elif choose == "下线":
            del dict1[username]
            print('\033[1;34;43m用户%s已下线\033[0m' % username)
    except Exception:
        continue

