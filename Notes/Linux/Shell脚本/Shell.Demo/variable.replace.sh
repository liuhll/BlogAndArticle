#!/bin/bash

echo ${var:-"Variable is not set"}
echo "1 - Value of var is ${var}"

echo ${var:="Variable is not set"}
echo "2 - Value of var is ${var}"

unset var
echo ${var:+"This is default value"}
echo "3 - Value of var is $var"

var="Prefix"
echo ${var:+"This is default value"}
echo "4 - Value of var is $var"

echo ${var:?"Print this message"}
echo "5 - Value of var is ${var}"

# 执行该脚本将输出一下内容：
# ------------------------
# Variable is not set
#1 - Value of var is
#Variable is not set
#2 - Value of var is Variable is not set
#3 - Value of var is
#This is default value
#4 - Value of var is Prefix
#Prefix
#5 - Value of var is Prefix