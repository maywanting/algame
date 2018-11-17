Trapping Rain Water
---

# Description

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example:

```
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

# Solution

First solution when i came up with this problem is using stack. Find the left side and find the right side, and then calculate the rain part.

But the most important problem is the definition about left side and right side. I think I haven't deal with this until I see other's solution of this problem after I solved.

So I try to find the pole, which determine the height of rain part. Poles have these features

- concave
- at least larger than one side, no matter left side or right side
- still be pole in poles we calculate from the array.

Third feature make sure the pole to determine the rain part.

Here is the program. Actually, the solution that moving left pointer and right pointer is really nice. This makes me think about the quick sort algorithm.
