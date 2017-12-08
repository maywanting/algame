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
        // System.out.println(res);

        return (res == origin);
    }

    public static void main(String[] args) {
        int num1 = 343; //true
        int num2 = -2147447412; //false
        Solution testClass = new Solution();
        System.out.println(testClass.isPalindrome(num1));
        System.out.println(testClass.isPalindrome(num2));
    }
}
