#!/bin/sh

chmod 755 /etc/init.d/ipv6tb
update-rc.d ipv6tb defaults
/etc/init.d/ipv6tb start