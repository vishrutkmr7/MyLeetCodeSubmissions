class Solution:
    def uniqueOccurrences(self, nums: List[int]) -> bool:
        count = Counter(nums)
        return len(count.values()) == len(set(count.values()))