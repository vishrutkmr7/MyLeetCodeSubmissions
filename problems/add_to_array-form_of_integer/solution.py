class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        n = len(num)
        for i in range(n - 1, -1, -1):
            num[i], k = (num[i] + k) % 10, (num[i] + k) // 10
        if k != 0:
            return [int(val) for val in str(k)] + num
        return num
