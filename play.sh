#!/bin/bash 

cat $1 | while read line ; do
    beep -f $(echo $line | cut -d , -f 1 -) -l $(echo $line | cut -d , -f 2 -)
done    
