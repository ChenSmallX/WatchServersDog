# WatchServersDog
a bash script to monitor own servers or VPS base on python language which has a simply UI

基于Python和命令行的一个监控 VPS 的小程序。包含界面优化。

## 特点

- 占用资源小
- 只需要 Python3 就可以直接驱动
- ~~使用的是 mac 的 shell 命令，所以应该可以在 linux 和 unix 上用，但是 windows 应该不行~~
- 改为使用 `pxssh` 模块进行远程登录，所以可以在 windows 上使用

## 功能

- 测试服务器 ping 值
- 测试服务器 cpu 占用
- 测试服务器 ram 占用
- 查询服务器所在地区、运营商的信息
- coming soon...

## 使用方法

1. 克隆项目至本地

```bash
git clone https://github.com/ChenSmallX/WatchServersDog.git
cd WatchServersDog
```

2. 按照 server.txt.sample 的格式添加服务器，并改名为 server.txt

    ```bash
    e.g.
    name:localhost; ip:127.0.0.1; user:root; psd:xxx
    ```

    添加服务器信息有三个信息并且顺序为：名字（备注），IP 地址，用户名（可选），密码（可选）

    名字和 IP 之后用半角分号`;`结束，密码则不用

    若没有用户名或密码，则填 `null`

3. 启动脚本（会随项目更新而更改入口）

```bash
python collector.py
```

## 常见问题

暂不支持 ipv6

我就是个无名渣渣，以此项目作为 Python 的学习之旅，遇到问题请联系我 QAQ

各位大佬如果看到有写错的地方请指出，我会虚心学习的 TvT
