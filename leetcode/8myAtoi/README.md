String to Integer(atoi)
---

# Description

Implement atoi to convert a string to an integer.

### Hint

Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

### Notes

It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

## Requirements for atoi:

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

# Solution

I think this question is very boring. The algorithm is very simple, but, there are too many requirements to be considered. So it is not surprised that there so many people who dislike this question.

I use C++ to solve this question.

``` C++
class Solution {
    public:
    int myAtoi(string str) {
        long int res = 0;
        int minusflag = -1;
        int flag = 0;
        for (int i = 0; i < str.length(); i++) {
            int ascii = str[i];
            if (ascii >= 48 && ascii <= 57) {
                res = res*10 + (ascii - 48);
                if (res >= 2147483648) {
                    break;
                }
                flag = 1;
            } else if (ascii == 45) { //负数
                if (minusflag != -1) {
                    return 0;
                }
                minusflag = 1;
                flag = 1;
            } else if (ascii == 43) { //正数符号
                if (minusflag != -1) {
                    return 0;
                }
                minusflag = 0;
                flag = 1;
            } else if (flag) {
                break;
            } else if (ascii == 32) {
                continue;
            } else {
                break;
            }
        }
        if (minusflag == 1) {
            res = 0 - res;
        }
        if (res > 2147483647) {
            return 2147483647;
        }
        if (res < -2147483648) {
            return -2147483648;
        }
        return res;
    }
};
```
