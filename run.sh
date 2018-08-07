
#set -m
#python record.py & python call.py && fg
#parallel ::: python record.py python call.py 
#killall python record.py

python record.py &
P1=$!
python call.py &
P2=$!
wait $P1 $P2
killall python record.py
rm -rf /home/mahima/images/*
#cd /home/mahima/images 
#del *.* /F /S /Q /A: R /A: H /A: 
#rmdir /home/mahima/images
#mkdir /home/mahima/images
