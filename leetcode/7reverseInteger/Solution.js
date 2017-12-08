#!/usr/bin/env node
var getReverseNum = function(x) {
    let res = 0;
    while(x > 0) {
        let num = x % 10;
        x = (x - num) / 10;
        res = res * 10 + num;
        console.log(x);
    }
    return res;
};

var reverse = function(x) {
    let res = 0;
    if (x < 0) { //负数情况
        let num = -x;
        res = -getReverseNum(num);
    } else {
        res = getReverseNum(x);
    }

    console.log(res);
    //32-bit range
    if ((res > 2147483648) || (res < -2147483648)) {
        return 0;
    } else {
        return res;
    }
};

let num1 = 123;
let num2 = -123;
let num3 = 130;
let num4 = 1534236469;
let num5 = 2147483648;
let num6 = 9646324351;
let num7 = 4294967296;

let res = reverse(num4);
console.log(res);
