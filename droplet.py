#!/anaconda3/bin/python python
# -*- coding: utf-8 -*-

from pexpect import pxssh
import getpass

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

    def login(self):
        if self.__is_connect:
            return True
        elif not self.__is_connect:
            try:
                ip = self.__ip
                user = self.__user
                password = self.__password
                self.__connection.login(server=ip, username=user, password=password)
            except pxssh.ExceptionPxssh:
                return False
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
                return True

    @property
    def connection(self):
        return self.__connection


def main():
    ip = input("input ip: ")
    user = input("input user: ")
    password = getpass.getpass("password: ")

    drop = droplet("temp", ip, user, password)
    drop.login()
    if drop.is_connect:
        print(drop.name+" is connected")
    else:
        print(drop.name+" is connect faired")
    
    if drop.is_connect:
        if drop.logout():
            print(drop.name+" logout successed")
        else:
            print(drop.name+" id login, but logout faired")
    else:
        pass


if __name__ == "__main__":
    main()
