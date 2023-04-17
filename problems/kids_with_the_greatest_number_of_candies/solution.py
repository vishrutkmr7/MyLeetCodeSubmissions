class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        gauge = max(candies) - extraCandies 
        return [candy >= gauge for candy in candies]