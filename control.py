#!/anaconda3/bin/ python
# -*- coding: utf-8 -*-

from droplet import droplet
import shell


def get_server_info(strInfo):
    """
    get name, ip and password from a string 
    info which from ping information
    """
    # get name
    name = strInfo[strInfo.index("name:")+5:strInfo.index(";")]
    strInfo = strInfo[strInfo.index(";")+1:]
    # get ip
    ip = strInfo[strInfo.index("ip:")+3:strInfo.index(";")]
    strInfo = strInfo[strInfo.index(";")+1:]
    # get password
    password = strInfo[strInfo.index("psd:")+4:strInfo.index("\n")]

    return name, ip, password


def get_servers(f_servers):
    servers = []

    strInfo = f_servers.readline()
    while strInfo:
        name, ip, password = get_server_info(strInfo)
        tempDroplet = droplet(name, ip, password)
        servers.append(tempDroplet)

        strInfo = f_servers.readline()  # 这一步要求 servers.txt 文件要有最后一行空行

    return servers


def print_server(server):
    print(server.name)
    print(server.ip)
    print(server.password)


def test_group_ping_once(servers):
    for ser in servers:
        print("ping:", ser.name, ":", end='')
        time = shell.ping(ser)  # maybe reture time as a float or s"timeout"
        print(time)


if __name__ == "__main__":
    # Watch-Server-Dog/ (when debug, contact it before the path)
    f_servers = open("server.txt", "r")
    servers = get_servers(f_servers)

    for ser in servers:
        print_server(ser)
        print("")

    test_group_ping_once(servers)

    f_servers.close()
