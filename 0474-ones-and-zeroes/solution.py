from collections import Counter


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        res = []
        counts = [(Counter(bins)['0'], Counter(bins)['1']) for bins in strs]
        def calc_max_subset_len(i, zeros, ones):
            if memo[i][zeros][ones] != -1:
                return memo[i][zeros][ones]
            if i == len(counts):
                memo[i][zeros][ones] = 0
                return 0
            pick = -1
            item_zeros, item_ones = counts[i][0], counts[i][1]
            if zeros - item_zeros >= 0 and ones - item_ones >= 0:
                pick = 1 + calc_max_subset_len(i + 1, zeros - item_zeros, ones - item_ones)
            skip = calc_max_subset_len(i + 1, zeros, ones)
            memo[i][zeros][ones] = max(pick, skip)
            return memo[i][zeros][ones]
        
                
        memo = [[[-1] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs) + 1)]
        
        return calc_max_subset_len(0, m, n)
