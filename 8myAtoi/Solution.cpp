#include <iostream>

using namespace std;

class Solution {
    public:
    int myAtoi(string str) {
        // cout << str.length() << " " << str << endl;
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
            // cout << res << endl;
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

int main() {
    Solution testSolution;
    string test1 = " -23513  "; // -23513
    string test2 = "+-2"; //0
    string test3 = ""; //0
    string test4 = "  -0012a42"; //-12
    string test5 = "    +0a32"; //0
    string test6 = "2147483648"; //2147483647
    string test7 = "   - 321"; //0
    string test8 = " ++1"; //0
    string test9 = " b11228552307"; //0
    string test10 = "123  456"; //0
    cout << testSolution.myAtoi(test1) << endl;
    cout << testSolution.myAtoi(test2) << endl;
    cout << testSolution.myAtoi(test3) << endl;
    cout << testSolution.myAtoi(test4) << endl;
    cout << testSolution.myAtoi(test5) << endl;
    cout << testSolution.myAtoi(test6) << endl;
    cout << testSolution.myAtoi(test7) << endl;
    cout << testSolution.myAtoi(test8) << endl;
    cout << testSolution.myAtoi(test9) << endl;
    cout << testSolution.myAtoi(test10) << endl;
    return 0;
}
