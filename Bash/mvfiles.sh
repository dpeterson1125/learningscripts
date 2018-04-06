#!/bin/bash
#This bash script will take a directory full of files with spaces in them
#then filter out any that do not meet the grep condition
#this grep ensures that the 2..- is there, dot dot can be any variable
#the IFS is a system variable that sets variables, in this case space
#https://bash.cyberciti.biz/guide/$IFS
#https://www.cyberciti.biz/tips/handling-filenames-with-spaces-in-bash.html
#I used this to clean up a folder that didn't organize the files very well and to purge out
#podcasts under episode 200
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
for i in $(ls | grep 2..-);
do
  mv "$i" 200plus/
done
IFS=$SAVEIFS
