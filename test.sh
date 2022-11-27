#!/bin/bash
while IFS= read -r line
do
    /home/harshini/project_HST_images/runjob.sh $line
    done<"/home/harshini/project_HST_images/COS.csv"
