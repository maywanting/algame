#!/bin/bash
# for example: ./newPractice.sh 1 test py

args=("$@")
length=${#args[@]}

if [ ! $length -eq 3 ]; then
    echo "./newPractice.sh 1 projectname py"
    exit 1
fi

number=$1
name=$2

case $3 in
    py)
        fileContent="class Solution(object):
    def $name(self):

solution = Solution()"
        ;;
    c)
        fileContent="$name() {
}

int main() {
    return 0;
}"
        ;;
    cpp)
        fileContent="#include <iostream>

using namespace std;

class Solution {
public:
    $name() {
    }
};

int main() {
    return 0;
}"
        ;;
    *)
        echo "no such type"
        exit 1
        ;;
esac

mkdir $number$name
echo "$fileContent" >> $number$name"/Solution."$3

echo "
---

# Description

# Solution
" >> $number$name"/README.md"

exit 0
