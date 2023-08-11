class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        prev = [0 for i in range(amount + 1)] 
        curr = [0 for i in range(amount + 1)] 
        for i in range(amount + 1):
            if i % coins[0] == 0:
                prev[i] = 1 
            else:
                prev[i] = 0
        for i in range(1,len(coins)):
            for j in range(amount + 1):
                nottake = prev[j]
                take=0
                if j >= coins[i]:
                    take = curr[j - coins[i]]
                curr[j] = take+nottake 
            prev = curr[:]
        return prev[amount] 
