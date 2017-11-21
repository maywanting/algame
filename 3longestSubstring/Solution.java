/**
 * title: Longest Substring Without Repeating Characters
 * description: Given a string, find the length of the longest substring without repeating characters.
 */

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
            // System.out.println(tempLong);
            return tempLong.length();
        } else {
            // System.out.println(nowLong);
            return nowLong.length();
        }
    }

    public static void main(String[] args) {
        String s1 = "abcabcbb";
        String s2 = "bbbbbb";
        String s3 = "pwwkew";
        Solution testClass = new Solution();
        System.out.println(testClass.lengthOfLongestSubstring(s1));
        System.out.println(testClass.lengthOfLongestSubstring(s2));
        System.out.println(testClass.lengthOfLongestSubstring(s3));
    }
}
