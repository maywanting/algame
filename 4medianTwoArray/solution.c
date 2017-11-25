#include <stdio.h>

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int sum = nums1Size + nums2Size;
    int all[sum];
    int index1 = 0, index2 = 0;
    int flag = (sum % 2 == 0);
    while ((index1 + index2) < sum) {
        if (index1 >= nums1Size) {
            all[index1 + index2] = nums2[index2];
            index2++;
        } else if (index2 >= nums2Size) {
            all[index1 + index2] = nums1[index1];
            index1++;
        } else if (nums1[index1] > nums2[index2]) {
            all[index1 + index2] = nums2[index2];
            index2++;
        } else {
            all[index1 + index2] = nums1[index1];
            index1++;
        }
    }

    if (flag) { // even number
        return (all[sum/2] + all[sum/2 - 1]) / 2.0;
    } else { // odd number
        return all[(sum - 1) / 2];
    }
}

double findMedianSortedArrays_old(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int index1 = 0, index2 = 0;
    int median, now, last;
    int temp[2] = {0, 0};
    //if one array is empty, add two number in it
    if (nums1Size == 0 && nums2Size == 0) {
        return 0.0;
    } else if (nums2Size == 0) {
        temp[0] = nums1[0] - 1;
        temp[1] = nums1[nums1Size - 1] + 1;
        nums2 = temp;
        nums2Size += 2;
    } else if (nums1Size == 0) {
        temp[0] = nums2[0] - 1;
        temp[1] = nums2[nums2Size - 1] + 1;
        nums1 = temp;
        nums1Size += 2;
    }

    if ((nums1Size + nums2Size) % 2 == 0) { //even number
        median = (nums1Size + nums2Size) / 2;
        while (index1 + index2 + 2 <= median) {
            if (nums1[index1] > nums2[index2]) {
                last = nums2[index2];
                index2++;
            } else {
                index1++;
            }
        }
        printf("%d %d\n", index1, index2);
        if (nums1[index1] > nums2[index2]) {
            return (nums2[index2] + last) / 2;
        } else {
            return (nums1[index1] + last) / 2;
        }
    } else { //odd number
        median = (nums1Size + nums2Size + 1) / 2;
        while (index1 + index2 + 2 <= median) {
            if (nums1[index1] > nums2[index2]) {
                index2++;
            } else {
                index1++;
            }
        }
        /* printf("%d %d\n", index1, index2); */
        return (nums1[index1] > nums2[index2]) ? nums2[index2] : nums1[index1];
    }
}

int main() {
    /* int num1[2] = {1, 2}; */
    /* int num2[2] = {3, 4}; */
    int num1[2] = {2, 3};
    int num2[0] = {};
    double res = findMedianSortedArrays(num1, 2, num2, 0);
    printf("%f", res); return 0;
}
