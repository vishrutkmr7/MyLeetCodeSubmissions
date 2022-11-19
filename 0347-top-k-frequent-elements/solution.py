class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sortedNums = sorted(freq.items(), key=lambda kv:(kv[1], kv[0])) 
        ans, n = [], len(sortedNums)
        for i in range(n - 1, -1, -1):
            if k==0: break
            ans.append(sortedNums[i][0])
            k -= 1
        return ans
        
