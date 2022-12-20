class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        one = set()
        double = set()
        for n in nums:
            if n not in one:
                one.add(n)
            else:
                double.add(n)
                
        return list(one - double)