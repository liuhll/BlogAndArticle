#!/bin/bash

#-------------------------------------------#
# 脚本进入死循环直至用户输入数字大于5                                          #  
#-------------------------------------------#

while :
do
    echo -n "Input a number between 1 to 5: "
    read aNum
    case $aNum in
        1|2|3|4|5) echo "Your number is $aNum!"
        ;;
        *) echo "You do not select a number between 1 to 5, game is over!"
            break
        ;;
    esac
done