#!/usr/bin/env bash

website = $1
interval = '60'
if [ $2 != '' ]
  then
    interval = $2
fi

echo $website
echo $interval
#python3 logger.py $website $interval    