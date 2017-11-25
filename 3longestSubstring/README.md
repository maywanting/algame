Longest Substring Without Repeating Characters
---

# Description

Given a string, find the length of the longest substring without repeating characters.

# Examples

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Solution

This problem is very easy. The most important thing is when finding a repeating character, how to make it out.

According to my solution, there are two string variables. The first is recording the longest string in history. Second is to record the string to be the longest string now. if finding the repeating character in nowString, then will update the history longest string and remove the character before the repeating character and itself in nowString.

I use Java to solve this problem

``` Java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        String nowLong = "";
        String tempLong = "";
        for (int i = 0; i < s.length(); i++) {
            int index = tempLong.indexOf(s.charAt(i));
            //not in tempLong
            if (index < 0) {
                tempLong += s.charAt(i);
            } else { //in tempLong
                if (nowLong.length() < tempLong.length()) {
                    nowLong = tempLong;
                }
                tempLong = tempLong.substring(index + 1) + s.charAt(i);
            }
        }
        if (tempLong.length() > nowLong.length()) {
            return tempLong.length();
        } else {
            return nowLong.length();
        }
    }
```

By the way, when running the java in CLI, `javac` commond is to compile the java code and `java` is to run the code compling be the `javac`.
