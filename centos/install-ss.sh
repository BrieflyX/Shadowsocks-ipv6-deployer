#!/bin/sh

# intall some package & quickly get shadowsocks configured.
# for centos, fedora

yum install epel-release &> /dev/null
yum update  &> /dev/null

wait

yum install python-setuptools m2crypto supervisor &> /dev/null

wait

easy_install pip &> /dev/null
pip install shadowsocks &> /dev/null

wait

cp shadowsocks.json /etc/shadowsocks.json
cp ss-supervisor.conf /etc/supervisor/conf.d/ss.conf
service supervisord start