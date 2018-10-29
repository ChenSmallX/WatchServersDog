#!/anaconda3/bin/python python
# -*- coding: utf-8 -*-

# pxssh 封装了 ssh 登录的各种方法
from pexpect import pxssh
# getpass 是获取密码时候反显星号或者空格
import getpass
# os 模块可执行系统命令等等
import os


class droplet(object):
    '''class to store information of server
    initialization:
        argument:
            name(str),
            ip(str),
            password(str)

    mathod:
        name, ip, password, and so on
    '''

    # set a limitation to droplet jest can have certain attributions
    # __slot__ = ('__name', '__ip', '__password', '__user', 'information')

    def __init__(self,
                 name="localhost",
                 ip="127.0.0.1",
                 user="null",
                 password="null"):
                # 默认服务器为 localhost
                # some thing to do: 加入参数【 ssh 端口】
        # basic attributes
        if isinstance(name, str):  # 检查 name 是否为字符串 string
            self.__name = name
        else:
            print('the name "', name, '" is not a str')

        if isinstance(ip, str):  # 检查 ip 是否为字符串
            self.__ip = ip
        else:
            print('the ip "', ip, '" is not a str')

        if isinstance(user, str):  # 检查 user 是否为字符串
            self.__user = user
        else:
            print('the username "', user, '" is not a str')

        if isinstance(password, str):  # 检查 password 是否为字符串
            self.__password = password
        else:
            print('the password "', password, '" is not a str')

        # initialize advanced attributes
        self.__is_connect = False           # 是否链接 ssh 的 flag
        self.__connection = pxssh.pxssh()   # 内置一个 pxssh 对象
        self.__result = "null"              # pxssh 执行命令后的返回串
        self.__local = "null"               # 所在地，由 curl cip.cc 获得
        self.__isp = "null"                 # 同上
        # preformance attributes
        self.__total_ram = 0  # MB          # 内存总量
        self.__total_disk = 0  # GB         # 硬盘总量
        # self.__boot_time = "d days, m min"

    # property 为修饰符，之后直接使用 drop.name 即可直接调用此方法
    # python will call this method when user call the name attribute
    @property
    def name(self):
        return self.__name

    # setter 同为修饰符，当对 drop.name 赋值的时候会调用此方法
    # python will call this method when user set the value of name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def ip(self):
        return self.__ip

    @ip.setter
    def ip(self, ip):
        self.__ip = ip

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def is_connect(self):
        return self.__is_connect

    @property
    def connection(self):
        return self.__connection

    @property
    def local(self):
        if self.__local == "null":
            self.renew_location()
        return self.__local

    @property
    def isp(self):
        return self.__isp

    @property
    def result(self):
        return self.__result

    @property
    def total_disk(self):
        return self.__total_disk

    @property
    def total_ram(self):
        return self.__total_ram

    @property
    def boot_time(self):
        return self.boot_time

    # 登录远程服务器方法
    # the method which would be used to login the remote servers
    def login(self):
        # 首先检查是否已经连上
        if self.__is_connect:
            return True
        elif not self.__is_connect:
            try:
                ip = self.__ip
                user = self.__user
                password = self.__password
                self.__connection.login(
                    server=ip, username=user, password=password)
            except pxssh.ExceptionPxssh:
                # this cause maybe cannot connect to server
                # or wrong password
                return False
            except AssertionError:
                '''one pxssh cannot login twice,and AssertionError
                would be thouw out when login twice. so reconduct a
                pxssh object can solve this problem
                一个 pxssh 对象只能登录一次，若 logout 一个 pxssh 后，则
                需要使用一个新的 pxssh 对象。
                '''
                self.__connection = pxssh.pxssh()
                return self.login()
            else:
                # 此时为 try 之间代码执行成功的情况
                # code got this block, the code try successed
                self.__is_connect = True
                return True

    # 登出远程服务器的方法
    # the method which would be used to logout the remote servers
    def logout(self):
        if not self.__is_connect:  # 检查是否连上
            return True  # 没连上的，logout 直接返回 True
        elif self.__is_connect:
            try:
                self.__connection.logout()  # 调用 pxssh 的 logout 可直接在远程 exit
            except OSError:
                print("cause the OSError")
                return False
            else:
                self.__is_connect = False
                return True

    # 执行命令方法
    def execute(self, commend):
        if not self.__is_connect:
            return False
        else:
            send_success = self.__connection.sendline(commend)
            if send_success:
                self.__connection.prompt()
                result_line = self.__connection.before[len(commend) + 2:-2]
                self.__result = result_line
                return True
            else:
                self.__result = "null"
                return False

    def ping(self):
        ping_return_info = os.popen("ping " + self.__ip + " -c 1", "r")
        queue = ping_return_info.readline()
        queue = ping_return_info.readline()

        try:
            str_time = queue[queue.index("time=") + 5:queue.index(" ms")]
        except BaseException:
            time = "timeout"
        else:
            time = float(str_time)

        return time

    def renew_location(self):
        try:
            local_return_info = os.popen("curl cip.cc/" + self.__ip, "r")
            str_temp_line = local_return_info.readline()

            str_temp_line = local_return_info.readline()
            self.__local = str_temp_line[str_temp_line.index(":") + 2:-1]

            str_temp_line = local_return_info.readline()
            self.__isp = str_temp_line[str_temp_line.index(":") + 2:-1]
        except ValueError:
            print("cannot get location infomation")
            return False

    def __str__(self):
        return str(self.__name + "\n" + self.__ip + "\n" + self.__user + "\n" +
                   self.__password)

    def cpu(self):
        if not self.__is_connect:
            return False
        elif self.execute("uptime"):
            uptime_info = str(self.result)
            # self.__boot_time = uptime_info[uptime_info.index("up") + 3:
            #                               uptime_info.index("min") + 3]
            s_load = uptime_info[uptime_info.index("age:") + 5:-1]
            ave1, ave5, ave15 = s_load[:-1].split(", ")
            return ave1, ave5, ave15
        else:
            return False

    def ram(self):
        if not self.is_connect:
            return False
        elif self.execute("free"):
            free_info = str(self.result)
            free_info = free_info[free_info.index("Mem"):]
            free_info = free_info[:free_info.index("\\r\\n") - 7]
            for i in range(1, 6):
                free_info = free_info.replace("  ", " ")
            l_free_info = free_info.split(" ")
            self.__total_ram = int(l_free_info[1])
            used = int(l_free_info[2])
            # free = int(l_free_info[3])
            return float(used) / float(self.__total_ram)
        else:
            return False

    def disk_rank(self):
        pass

    def disk_io(self):
        pass


# function in main
def main_login(drop):
    if drop.is_connect:
        print(drop.name, " is already login")
        return True
    elif drop.login():
        print(drop.name, " connect success")
        return True
    else:
        print(drop.name, " connect failed")
        return False


def main_logout(drop):
    if drop.is_connect:
        if drop.logout():
            print(drop.name, " logout success")
            return True
        else:
            print(drop.name, " logout failed")
            return False
    else:
        print(drop.name, " is already logout")
        return True


def main_ping(drop):
    print("ping", drop.name, ":", drop.ping(), "ms")


def main_info(drop):
    print(drop.name, "basic infomation:")
    print("ip: ", drop.ip)
    print(drop.name, " locate in:\n", drop.local)


def main_exec(drop):
    if drop.is_connect:
        while True:
            command = input(drop.name, " >> ", end='')
            result = drop.exec(command)
            if result:
                print("execute succeed\nresult is:")
                print(drop.result)
                return True
            else:
                print("execute faild.")
                return False
    else:
        print(drop.name, ' is not connected.')
        return False


def main():
    droplets = []
    input_mode = input("manual(1) file(2): ")
    drop = droplet()

    if input_mode == "1":
        ip = input("input ip: ")
        user = input("input user: ")
        password = getpass.getpass("password: ")

        drop = droplet("temp", ip, user, password)
        droplets.append(drop)

    elif input_mode == "2":
        import reader
        droplets = reader.get_servers("server.txt")
        if len(droplets) == 0:
            print("no server in file")
            exit()

        i = 1
        for ser in droplets:
            print(i, ":", ser.name)
            i = i + 1
        i = int(input("choose one: "))
        # print(len(droplets))
        if i < len(droplets)+1:
            drop = droplets[i - 1]
        else:
            print("input error")
            exit()

    else:
        print("input error")
        exit()

    while True:
        if not drop.is_connect:
            print('1. login\n2. logout\n3. ping\n4. info\n0. exit')
        elif drop.is_connect:
            print('1. login\n2. logout\n3. ping\n4. info\n5.exec\n0. exit')

        commend = input("> ")
        if commend == '\n':
            continue
        fun = {
            '0': exit,
            '1': main_login,
            '2': main_logout,
            '3': main_ping,
            '4': main_info,
            '5': main_exec,
        }.get(commend)

        if commend == '0':
            if drop.is_connect:
                drop.logout()
            exit(0)
        else:
            fun(drop)


if __name__ == "__main__":
    main()
