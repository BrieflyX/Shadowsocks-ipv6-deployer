#!/bin/sh

apt-get install gcc &> /dev/null
gcc tb_userspace.c -l pthread -o tb_userspace
cp tb_userspace /usr/local/bin/tb_userspace