#!/bin/sh

# intall some package & quickly get shadowsocks configured.
# for debian, ubuntu

apt-get install python-setuptools m2crypto supervisor &> /dev/null
easy_install pip &> /dev/null
pip install shadowsocks &> /dev/null

cp shadowsocks.json /etc/shadowsocks.json
cp ss-supervisor.conf /etc/supervisor/conf.d/ss.conf
service supervisord start