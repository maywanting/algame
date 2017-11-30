Reverse Integer
---

# Description

Given a 32-bit signed integer, reverse digits of an integer.

##example1

```
Input: 123
Output: 321
```

##example2

```
Input: -123
Output: -321
```

##example3

```
Input: 120
Output: 21
```

##Note:

Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows. 

# Solution

This problem is very easy. The only one point is the 32-bit signed integer range. 32-bit integer means `2^31`, not `2^32`, because of the first bit is to be signed as negative number or not.

I use Javascript to solve this problem.

``` Javascript
var getReverseNum = function(x) {
    let res = 0;
    while(x > 0) {
        let num = x % 10;
        x = (x - num) / 10;
        res = res * 10 + num;
    }
    return res;
};

var reverse = function(x) {
    let res = 0;
    if (x < 0) { //negative number
        let num = -x;
        res = -getReverseNum(num);
    } else {
        res = getReverseNum(x);
    }

    //32-bit range
    if ((res > 2147483648) || (res < -2147483648)) {
        return 0;
    } else {
        return res;
    }
};
```
