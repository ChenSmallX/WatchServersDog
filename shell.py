#!/anaconda3/bin/python python
# -*- coding: utf-8 -*-

import os

# from droplet import droplet


# useless, droplet class has a ping member method
def ping(server):
    '''return the ping value one time
    argument: server (droplet class)
    return: time (would be a float or a s"timeout")

    cause: The ping commend can return a series of
    information about the network connection status
    to target server.
    use the argument "-c" and attach one number
    after that can do the ping for a certain times
    of the number.
    We get the 2nd line of the returned information
    (because the 1st line is a prompt) to extract the
    time of ping.
    '''
    ping_info = os.popen("ping " + server.ip + " -c 1", "r")
    info0 = ping_info.readline()
    info0 = ping_info.readline()

    # cause the ping commend would be timeout,
    # so when exception, must be ping timeout
    try:
        str_time = info0[info0.index("time=")+5: info0.index(" ms")]
    except BaseException:
        time = "timeout"
    else:
        time = float(str_time)

    return time


def get_shell_size():
    '''get lines and columns of current shell
    return: lines, columns

    cause: In unix/linux shell, the commend "echo
    $LINES" and "echo $COLUMNS" can return the
    size of this shell
    '''
    lines = int(os.popen("echo $LINES", "r").readline()[:-1])
    columns = int(os.popen("echo $COLUMNS", "r").readline()[:-1])
    return lines, columns


# useless, droplet class has a location attribute
def get_location_info(server):
    '''
    argument: server (droplet class)
    return: location, isp

    cause: post to "cip.cc" can return the information
    of the ip location which attach after the url
    '''
    str_info = os.popen("curl cip.cc/" + server.ip, "r")
    index1 = str_info.index("地址    : ")+len("地址    : ")
    index2 = str_info.index("运营商  : ")-1
    str_location = str_info[index1: index2]

    index1 = str_info.index("运营商  : ")+len("运营商  : ")
    index2 = str_info.index("数据二  : ")-2
    str_isp = str_info[index1: index2]

    return str_location, str_isp


if __name__ == "__main__":
    print(os.get_terminal_size().columns)
    exit()
