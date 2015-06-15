# Shadowsocks IPv6 Deployer

## Developed by BrieflyX

## 开发状态

基本功能已经写完了，不过还没有测试，有问题可以发issue。

## 简介

ss一键部署工具，附加ipv6通道建立工具。

在服务器上部署shadowsocks与6to4的隧道，省去繁琐的安装步骤。

使用supervisor监视SS服务器运行情况。

系统将自动检测Linux发行版类型，使用合适的包工具(apt-get or yum)以及开机脚本。无论CentOS，Fedora，还是Debian，Ubuntu，都可以轻松安装。

## 配置说明

配置文件是ss-deployer.conf需要填写ipv6的地址。ss-supervisor.conf是supervisor的配置文件一般不用改动，如果你需要设置可以自行修改。

如果你的VPS已经有ipv6地址（使用ifconfig查看），则不需要配置6to4隧道，直接连接就可以了（-s选项只安装shadowsocks）。

如果VPS没有ipv6地址，执行cat /dev/net/tun，显示File descriptor in bad state，则可以建立ipv6 tunnel。

如果VPS只有ipv4地址，则需要首先申请一个隧道服务[TunnelBroker](https://tunnelbroker.net/)，注册之后单击左侧的Create Regular Tunnel，填入VPS的ipv4地址选择一个比较合适的隧道服务器。然后在配置文件中填写以下内容

```
[shadowsocks]
server=::                                   # 服务器地址，::表示所有ipv4,ipv6的ip，不用修改
local_port=1080                             # 本地端口，不用修改
port_password=4000:password1;5000:password2;6000:password3  # 格式 port:password，用分号;隔开
timeout=600                                 # 超时，不用更改
method=aes-256-cfb                          # 加密方式，常用的有aes-256-cfb，rc4-md5等等。

[ipv6]
clientaddr=xx.xx.xx.xx                      # VPS的ipv4地址（Client IPv4 Address）
serveraddr=xx.xx.xx.xx                      # Server IPv4 Address
ipv6addr=2001:470:xx:xxx::2/64              # VPS的ipv6地址（Client IPv6 Address）
routeraddr=2001:470:xx:xxx::1/64            # 路由地址（在Routed /64地址的/64前加个1）
```

运行./ss-deployer，等待程序完成。
如果ping6 ipv6.google.com能够成功，则已经完成任务了。

## 参考资料

本文全流程参考这篇博文：[在搬瓦工等OPENVZ架构的CENTOS上安装Shadowsocks和建立IPV6完全教程](http://bpplpp.cn/moved-shadowsocks-installed-on-centos-openvz-architecture-such-as-bricklayer-and-set-up-ipv6-tutorial.html)

# Attention!

最后再唠叨几句，搭好ipv6以后客户端连接时填ipv6地址，嗯，两边要加一对中括号！究其原因，大概是由于ipv6地址中的冒号容易与URI中的端口指定搞混吧。

反正当初我配的时候连了半天没连上，接着发现坑在这.......

错误信息到/var/log/supervisor下查看。