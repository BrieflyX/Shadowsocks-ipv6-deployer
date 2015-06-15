#!/bin/sh

chmod 755 /etc/init.d/ipv6tb
chkconfig –add ipv6tb
/etc/init.d/ipv6tb start