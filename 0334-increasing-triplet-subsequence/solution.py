class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float(inf), float(inf)
        
        for third in nums:
            if second < third: return True
            if third <= first: first = third    
            else:  second = third 
                
        return  False
