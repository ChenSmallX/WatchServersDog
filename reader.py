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
    # get username
    user = strInfo[strInfo.index("user:")+5:strInfo.index(";")]
    strInfo = strInfo[strInfo.index(";")+1:]
    # get password
    password = strInfo[strInfo.index("psd:")+4:strInfo.index("\n")]

    return name, ip, user, password


def get_servers(s_f_server):
    f_servers = open(s_f_server, "r")
    servers = []

    strInfo = f_servers.readline()
    while strInfo:
        name, ip, user, password = get_server_info(strInfo)
        tempDroplet = droplet(name, ip, user, password)
        servers.append(tempDroplet)

        strInfo = f_servers.readline()  # 这一步要求 servers.txt 文件要有最后一行空行

    f_servers.close()
    return servers


def test_group_ping_once(servers):
    for ser in servers:
        print("ping:", ser.name, ":", end='')
        time = shell.ping(ser)  # maybe reture time as a float or s"timeout"
        print(time)


def main():
    # Watch-Server-Dog/ (when debug, contact it before the path)
    servers = get_servers("server.txt")

    for ser in servers:
        print(ser, end='\n\n')

    # test_group_ping_once(servers)
    for ser in servers:
        print(ser.name+":", ser.ping())


if __name__ == "__main__":
    main()
