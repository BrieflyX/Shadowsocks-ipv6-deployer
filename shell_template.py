startup_shell = '''#!/bin/sh

### BEGIN INIT INFO
# Provides: ipv6
# Required-Start: $local_fs $all
# Required-Stop: $local_fs $network
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: starts the ipv6 tunnel
# Description: ipv6 tunnel start-stop-daemon
### END INIT INFO

# /etc/init.d/ipv6tb

touch /var/lock/ipv6tb

case "$1" in
start)
echo "Starting ipv6tb"
setsid ./tb_userspace tb %s %s sit
sleep 3s
ifconfig tb up
ifconfig tb inet6 add %s
ifconfig tb inet6 add %s
ifconfig tb mtu 1480
route -A inet6 add ::/0 dev tb
route -A inet6 del ::/0 dev venet0
;;
stop)
echo "Stopping ipv6tb"
ifconfig tb down
route -A inet6 del ::/0 dev tb
killall tb_userspace
;;
*)
echo "Usage: /etc/init.d/ipv6tb {start|stop}"
exit 1
;;
esac

exit 0
'''