class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        i = win_of_make_satisfied = satisfied = max_make_satisfied = 0
        for c, g in zip(customers, grumpy):
            satisfied += (1 - g) * c
            win_of_make_satisfied += g * c
            if i >= X:
                win_of_make_satisfied -= grumpy[i - X] * customers[i - X]
            max_make_satisfied = max(win_of_make_satisfied, max_make_satisfied)
            i += 1
        return satisfied + max_make_satisfied