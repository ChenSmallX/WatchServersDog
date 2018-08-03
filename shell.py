#!/anaconda3/bin/python python
# -*- coding: utf-8 -*-

import os
# from droplet import droplet


def ping(server):
    pingInfo = os.popen("ping " + server.getIP() + " -c 1", "r")
    info0 = pingInfo.readline()
    info0 = pingInfo.readline()

    try:
        strTime = info0[info0.index("time=")+5: info0.index(" ms")]
    except BaseException:
        time = "timeout"
    else:
        time = float(strTime)

    return time
