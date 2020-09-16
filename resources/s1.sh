IP=$(/sbin/ifconfig -a|grep inet|grep -v 127.0.0.1|grep -v inet6|awk '{print $2}'|tr -d "addr:");
MEMORY=$(free -m | awk 'NR==2{printf "%.2f%%", $3*100/$2 }');
DISK=$(df -h | awk '$NF=="/"{printf "%s", $5}');
CPU=$(top -bn1 | grep load | awk '{printf "%.2f%%", $(NF-2)}');
echo "$IP|$MEMORY|$DISK|$CPU";
