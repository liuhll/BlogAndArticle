#!/bin/sh
NAME[0]="Zara"
NAME[1]="Qadir"
NAME[2]="Mahnaz"
NAME[3]="Ayan"
NAME[4]="Daisy"
echo "First Index: ${NAME[0]}"
echo "Second Index: ${NAME[1]}"

echo "First Method: ${NAME[*]}"
echo "Second Method: ${NAME[@]}"

# 执行该脚本将输出以下内容
#----------------------
#First Index: Zara
#Second Index: Qadir
#First Method: Zara Qadir Mahnaz Ayan Daisy
#Second Method: Zara Qadir Mahnaz Ayan Daisy