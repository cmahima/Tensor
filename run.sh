#! /bin/bash
echo Hi... Welcome to CERAS lab

read -p "Press T to use Tensor and W to use Watson " varname

#read varname

#echo Face the camera
 



if  [[ $varname = T ]] ;
then
 echo Face the camera... 
 sleep 3
 cd tensor_client
 python video.py #& python test.py ; fg
 python test.py 
 killall python video.py
 rm -rf /home/turtle/images/*

else
 echo Face the camera...
 sleep 3
 cd
 cd watson_client
 python video.py #& python sample_script.py ; fg
 python run.py
 killall python video.py
 rm -rf /home/turtle/images/*
fi

