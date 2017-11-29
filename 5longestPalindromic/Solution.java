class Solution {

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
                System.out.println(j);
                System.out.println("++++++++++++===");
                if (s.charAt(i) == s.charAt(j) && this.judgePalindrome(s.substring(i, j+1))) {
                    maxStr = s.substring(i, j+1);
                }
            }
        }
        return maxStr;
    }

    public static void main(String[] args) {
        String s1 = "cbbdbb";
        String s2 = "a";
        String s3 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
        Solution testSolution = new Solution();
        // System.out.println(testSolution.longestPalindrome(s1));

        // System.out.println(testSolution.longestPalindrome(s2));
        System.out.println(testSolution.longestPalindrome(s3));
    }
}
