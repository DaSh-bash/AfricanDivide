#!/bin/bash
filename="chromnames.txt"
echo $filename
all_lines=$(cat $filename)
for line in $all_lines 
do
    #echo "$line"
    grep "$line" cardui_migrdiv_indv_rarev_md25.bim | wc -l  
done
