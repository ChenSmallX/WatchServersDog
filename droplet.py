#!/anaconda3/bin/python python
# -*- coding: utf-8 -*-

from pexpect import pxssh
import getpass
import os


class droplet(object):
    '''class to store information of server
    initialization:
        argument:
            name(str),
            ip(str),
            password(str)

    mathod:
        name, ip, password
    '''

    # set a limitation to droplet jest can have certain attributions
    # __slot__ = ('__name', '__ip', '__password', '__user', 'information')

    def __init__(self, name, ip, user, password):
        # basic attributes
        if isinstance(name, str):
            self.__name = name
        else:
            print('the name "', name, '" is not a str')

        if isinstance(ip, str):
            self.__ip = ip
        else:
            print('the ip "', ip, '" is not a str')

        if isinstance(user, str):
            self.__user = user
        else:
            print('the username "', user, '" is not a str')

        if isinstance(password, str):
            self.__password = password
        else:
            print('the password "', password, '" is not a str')

        # initialize advanced attributes
        self.__is_connect = False
        self.__connection = pxssh.pxssh()
        self.__result = "null"
        self.__local = "null"
        self.__isp = "null"
        # preformance attributes
        self.__total_ram = 0  # MB
        self.__total_disk = 0  # GB
        # self.__boot_time = "d days, m min"

    @property
    def name(self):
        return self.__name

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

    def login(self):
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
                '''
                self.__connection = pxssh.pxssh()
                return self.login()
            else:
                self.__is_connect = True
                return True

    def logout(self):
        if not self.__is_connect:
            return True
        elif self.__is_connect:
            try:
                self.__connection.logout()
            except OSError:
                return False
            else:
                self.__is_connect = False
                return True

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
        local_return_info = os.popen("curl cip.cc/" + self.__ip, "r")
        str_temp_line = local_return_info.readline()

        str_temp_line = local_return_info.readline()
        self.__local = str_temp_line[str_temp_line.index(":") + 2:-1]

        str_temp_line = local_return_info.readline()
        self.__isp = str_temp_line[str_temp_line.index(":") + 2:-1]

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
            free_info = free_info[:free_info.index("\\r\\n")-7]
            for i in range(1, 6):
                free_info = free_info.replace("  ", " ")
            l_free_info = free_info.split(" ")
            self.__total_ram = int(l_free_info[1])
            used = int(l_free_info[2])
            # free = int(l_free_info[3])
            return float(used)/float(self.__total_ram)
        else:
            return False

    def disk_rank(self):
        pass

    def disk_io(self):
        pass


def main():
    ip = input("input ip: ")
    user = input("input user: ")
    password = getpass.getpass("password: ")

    drop = droplet("temp", ip, user, password)
    drop.login()
    if drop.is_connect:
        print(drop.name + " is connected")

        commend = input("> ")
        if drop.execute(commend):
            print("execute success")
            print(drop.result)
        else:
            print("execute failed")
    else:
        print(drop.name + " is connect failed")

    if drop.is_connect:
        if drop.logout():
            print(drop.name + " logout successed")
        else:
            print(drop.name + " id login, but logout failed")
    else:
        pass


if __name__ == "__main__":
    main()
