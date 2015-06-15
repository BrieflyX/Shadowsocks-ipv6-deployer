#!/bin/sh

# intall some package & quickly get shadowsocks configured.
# for debian, ubuntu

apt-get install -y python-setuptools m2crypto supervisor &> /dev/null
wait
easy_install pip &> /dev/null
pip install shadowsocks &> /dev/null
wait
cp shadowsocks.json /etc/shadowsocks.json
cp ss-supervisor.conf /etc/supervisor/conf.d/ss.conf
service supervisord start