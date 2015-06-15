#!/bin/sh

yum install -y gcc gcc-c++ kernel-devel &> /dev/null
wait
gcc ../tb_userspace.c -l pthread -o ../tb_userspace
wait
cp ../tb_userspace /usr/local/bin/tb_userspace