class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_target_index = self.binary_search(
            nums,
            target,
            0,
            len(nums) - 1,
            lambda mid_value: mid_value >= target
        )
        
        if left_target_index == -1:
            return [-1, -1]
        
        right_target_index = self.binary_search(
            nums,
            target,
            0,
            len(nums) - 1,
            lambda mid_value: mid_value > target
        )
        
        return [left_target_index, right_target_index]
    
    def binary_search(self, nums: list[int], target: int, left: int, right: int, predicate):
        best_index_match = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                best_index_match = mid
            
            if predicate(nums[mid]):
                right = mid - 1
            else:
                left = mid + 1
            
        return best_index_match
        
