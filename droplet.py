#!/anaconda3/bin/python python
# -*- coding: utf-8 -*-


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
    # set a limitation to droplet jest can have 3 attribution
    __slot__ = ('__name', '__ip', '__password', '__user', 'information')

    def __init__(self, name, ip, user, password):
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
