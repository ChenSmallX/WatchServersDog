#!/anaconda3/bin/python python
# -*- coding: utf-8 -*-


class droplet(object):

    def __init__(self, name, ip, password):
        self.__name = name
        self.__ip = ip
        self.__password = password

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setIP(self, ip):
        self.__ip = ip

    def getIP(self):
        return self.__ip

    def setPassword(self, password):
        self.__password = password

    def getPassword(self):
        return self.__password
