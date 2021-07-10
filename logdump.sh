#!/bin/bash

lines="$(wc -l error_log.txt | cut -c1)"
now=`date +"%m_%d_%Y_%H_%M"
if [ $lines -gt 10000]
then
    new_file="error_log_$now.txt"
    touch "$new_file"
    cat error_log.txt >> "$new_file"
    : > error_log.txt
fi
