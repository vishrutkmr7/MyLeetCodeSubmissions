class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        frequency = Counter(tasks)
        res = 0
        for freq in frequency.values():
            if freq == 1:
                return -1
            res += 1 if freq == 2 else ceil(freq / 3)
        return res