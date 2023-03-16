class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        ptr1, ptr2 = 0, 0
        len1, len2 = len(nums1), len(nums2)
        total1, total2 = 0, 0
        mod = 10**9 + 7
        while ptr1 < len1 or ptr2 < len2:
            if ptr1 < len1 and (ptr2 == len2 or nums1[ptr1] < nums2[ptr2]):
                total1 += nums1[ptr1]
                ptr1 += 1
            elif ptr2 < len2 and (ptr1 == len1 or nums1[ptr1] > nums2[ptr2]):
                total2 += nums2[ptr2]
                ptr2 += 1
            else:
                total1 = total2 = max(total1, total2) + nums1[ptr1]
                ptr1 += 1
                ptr2 += 1

        return max(total1, total2) % mod
