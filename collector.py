#!/anaconda3/bin/ python
# -*- coding: utf-8 -*-

import reader


def renew_paper(servers):
    servers_paper = []
    return servers_paper


def main():
    servers = reader.get_servers("server.txt")
    servers_paper = renew_paper(servers)
    print(servers_paper)


if __name__ == "__main__":
    main()
