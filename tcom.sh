#!/bin/bash

sshpass -p "turtleroot" ssh -o StrictHostKeyChecking=no mahima@192.168.0.101 <<EOF
echo "------------INSIDE SERVER-------------"
collectl -sCD >& /home/mahima/collectl.txt&

exit
EOF

#echo "-------STARTING HTTPERF--------"
#sudo taskset -c 1 httperf --sever 130.63.174.60 --port=80 --uri=/consumecpu.php --num-conn=40000 --period=e0.0025 >& /home/turtle/result.txt&

sleep 2

echo "---------RUNNING CODE-----------"
 python test.py

#cd tensor_client
#python sample_script.py



sshpass -p "turtleroot" ssh -o StrictHostKeyChecking=no mahima@192.168.0.101 <<EOF
killall collectl
exit
EOF

