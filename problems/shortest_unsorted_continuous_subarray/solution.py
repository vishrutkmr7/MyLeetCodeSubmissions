class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        monotonic_stack = []
        indexes = []
        begin = None
        end = None
        cur_max = None

        for i in range(n):
            while monotonic_stack and nums[i] < monotonic_stack[-1]:
                val = monotonic_stack.pop()
                ind = indexes.pop()
                if begin is None or ind < begin:
                    begin = ind
                if cur_max is None or val > cur_max:
                    cur_max = val
                if end is None or i > end:
                    end = i
            if cur_max is not None and nums[i] < cur_max:
                end = i
            monotonic_stack.append(nums[i])
            indexes.append(i)

        return end - begin + 1 if begin is not None else 0