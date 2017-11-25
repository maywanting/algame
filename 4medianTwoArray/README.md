Median of Two Sorted Array
---

# Description

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Examples

example1

```
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
```

example2

```
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```

# Solutions

I think the most difficult of this problem is how to work out the empty array. In fact, I have wasted a lot of time in solving the empty array. So, the way to work out this problem is to merge two array to one array. This process is easy because of sorted. So find the median of one array will be very easy.

``` C
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
```

By the way, to run c program, `gcc` will be used to compile the program. And then the `a.out` file will be created. So excueting the `a.out` file and then to get the result.
