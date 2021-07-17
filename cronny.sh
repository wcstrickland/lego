#!/bin/bash

now="$(date +"%m_%d_%Y_%H_%M")"

new_file="error_log_$now.txt"
touch /home/lindsay/py/"$new_file"
echo $now  >> /home/lindsay/py/"$new_file"
