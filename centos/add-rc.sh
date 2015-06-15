#!/bin/sh

chmod 755 /etc/init.d/ipv6tb
wait
chkconfig –add ipv6tb
wait
/etc/init.d/ipv6tb start