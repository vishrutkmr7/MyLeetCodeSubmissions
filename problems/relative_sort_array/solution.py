class Solution:
    def relativeSortArray(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return sorted(nums1, key=(nums2 + sorted(nums1)).index)