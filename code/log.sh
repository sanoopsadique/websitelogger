#!/bin/sh

var website = $1
var interval = '60'
if [ $2 != '' ]
  then
    interval = $2
fi

echo $website
echo $interval
#python3 logger.py $website $interval    