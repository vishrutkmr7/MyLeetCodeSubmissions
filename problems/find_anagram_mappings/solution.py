class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {nums2[i]: i for i, _ in enumerate(nums2)}
        return [d[a] for a in nums1]