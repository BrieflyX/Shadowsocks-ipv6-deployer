#!/bin/sh

chmod 755 /etc/init.d/ipv6tb
wait
update-rc.d ipv6tb defaults
wait
/etc/init.d/ipv6tb start