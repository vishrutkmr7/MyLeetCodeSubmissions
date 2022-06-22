class Solution:
    def merge_sort(self, arr) -> List[int]:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return list(merge(left, right))
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return self.merge_sort(nums)[-k]
        return sorted(nums)[-k]
        
        
