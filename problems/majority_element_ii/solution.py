class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2, count1, count2 = None, None, 0, 0
        n = len(nums)
        
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        
        return list(set(candidate for candidate in [candidate1, candidate2] if nums.count(candidate) > n // 3))
