#!/anaconda3/bin/python python
# -*- coding: utf-8 -*-

from droplet import droplet
import os


class screen(object):
    '''the top layer --- screen class
    this class control the display on screen
    one screen object is one shell screen definatly
    '''

    def __init__(self):
        self.__columns = -1  # column 是横着的尺寸
        self.__lines = -1  # line 是竖着的尺寸
        self.__droplets = []

    @property
    def columns(self):
        if self.__columns == -1:
            self.renew_size()
        return self.__columns

    @property
    def lines(self):
        if self.__lines == -1:
            self.renew_size()
        return self.__lines

    def renew_size(self):
        size = os.get_terminal_size()
        self.__columns = size.columns
        self.__lines = size.lines


def main():
    screen_test = screen()
    print("shell size:")
    print("columns:", screen_test.columns, end=' ')
    print("lines:", screen_test.lines)


if __name__ == "__main__":
    main()
