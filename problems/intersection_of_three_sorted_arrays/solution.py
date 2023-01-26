class Solution:
    def arraysIntersection(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        return [
            key for key, value in Counter(nums1 + nums2 + nums3).items() if value == 3
        ]