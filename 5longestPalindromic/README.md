Longest Palindromic Substring
---

# Description
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Examples

example1

```
Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
```

example2

```
Input: "cbbd"

Output: "bb"
```

# Solutions

In fact, I don't have solved this problem. A lot of methods have been used, but, the result is "time limited".So, if I find other good ideas to deal with it, I will update this blog.

``` javascript
var judgePalindrome = function(s) {
    // return (s.split("").reverse().join("") == s);
    const len = s.length;
    for (let i = 0; i <= (len-i-1); i++) {
        if (s[i] !== s[len - i - 1]) {
            return false;
        }
    }
    return true;
};

var longestPalindrome = function(s) {
    let maxStr = "";
    let maxLength = 0;
    let length = s.length;
    for (let i = 0; i + maxLength < length; i++) {
        for (let j = length-1; j >= i + maxLength; j--) {
            let tempStr = s.substr(i, j-i+1);
            if (s[i] == s[j] && judgePalindrome(tempStr)) {
                maxStr = tempStr;
                maxLength = j+1-i;
            }
        }
    }
    return maxStr;
};
```

``` java
public Boolean judgePalindrome(String s) {
    int length = s.length();
    for (int i = 0; i <= (length-i-1); i++) {
        if (s.charAt(i) != s.charAt(length - 1 - i)) {
            return false;
        }
    }
    return true;
}

public String longestPalindrome(String s) {
    String maxStr = "";
    for (int i = 0; i + maxStr.length() < s.length(); i++) {
        for (int j = s.length() - 1; j >= i + maxStr.length(); j--) {
            if (s.charAt(i) == s.charAt(j) && this.judgePalindrome(s.substring(i, j+1))) {
                maxStr = s.substring(i, j+1);
            }
        }
    }
    return maxStr;
}
```
