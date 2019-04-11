Permutation Sequence
---

# Description

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

Given n and k, return the kth permutation sequence.

Note:

    Given n will be between 1 and 9 inclusive.
    Given k will be between 1 and n! inclusive.

Example 1:

Input: n = 3, k = 3
Output: "213"

Example 2:

Input: n = 4, k = 9
Output: "2314"

# Solution

I think when we permuate the number, the first character can be divided as the number of n. So, we need to find out sequence of first character.

Not considering about sort sequence of other characters. So we need to divide the condition of other characters and then we can gain the ith of sequence.

other character is also processed as above. One thing should be mentioned: if we find out the right character, we need to remove this character in candidate list.

``` python
class Solution(object):
    def getPermutation(self, n, k):
        flag = 1
        for i in range(1, n+1):
            flag *= i
        listN = [str(i) for i in range(1, n+1)]
        k -= 1
        res = ''
        for i in range(n, 0, -1):
            flag /= i
            index = k / flag
            k = k % flag
            res += listN[index]
            listN = listN[:index] + listN[index+1:]
        return res
```
