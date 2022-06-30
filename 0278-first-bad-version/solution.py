# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, mid, high = 1, n//2, n
        while (low <= high): 
            mid = (low + high) // 2
            if (isBadVersion(mid)): 
                if not (isBadVersion(mid - 1)): break
                high = mid - 1
            else: low = mid + 1
        return mid if mid > 0 else 1
