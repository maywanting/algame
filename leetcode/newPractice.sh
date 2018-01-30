#!/bin/bash

args=("$@")
length=${#args[@]}

if [ ! $length -eq 2 ]; then
    echo "wrong number"
    exit
fi

number=$1
name=$2

mkdir $number$name
touch $number$name"/README.md"

echo "
class Solution(object):
    def $name(self):

solution = Solution()
" >> $number$name"/Solution.py"
