#!/anaconda3/bin/python python
# -*- coding: utf-8 -*-

from droplet import droplet
import shell


def getServerInfo(strInfo):
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


def getServers(fServers):
    servers = []

    strInfo = fServers.readline()
    while strInfo:
        name, ip, password = getServerInfo(strInfo)
        tempDroplet = droplet(name, ip, password)
        servers.append(tempDroplet)

        strInfo = fServers.readline()  # 这一步要求 servers.txt 文件要有最后一行空行

    return servers


def printServer(server):
    print(server.getName())
    print(server.getIP())
    print(server.getPassword())


def testGroupPingOnce(servers):
    for ser in servers:
        print("ping:", ser.getName(), ":", end='')
        time = shell.ping(ser)  # maybe reture time as a float or s"timeout"
        print(time)


def main():
    # Watch-Server-Dog/ (when debug, contact it before the path)
    fServers = open("server.txt", "r")
    servers = getServers(fServers)

    for ser in servers:
        printServer(ser)
        print("")

    testGroupPingOnce(servers)


if __name__ == "__main__":
    main()
