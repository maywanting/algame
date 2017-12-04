Palindrome Number
---

# Description

Determine whether an integer is a palindrome. Do this without extra space.

Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

# Solution

This problem is similar with `Reverse Integer`. Actually, I use the same algorithm to solve this question.

The only one point is that negative number can not be palindrome number.

I use Java to solve this problem.

``` Java
class Solution {
    public boolean isPalindrome(int x) {
        if (x == 0) {
            return true;
        }
        if (x < 0) {
            return false;
        }

        int res = 0, num = 0, origin = x;
        while(x > 0) {
            num = x % 10;
            x = (x - num) / 10;
            res = res * 10 + num;
        }

        return (res == origin);
    }
}
```
