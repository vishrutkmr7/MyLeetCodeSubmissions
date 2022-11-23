class Solution:

    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        window = sorted(nums[:k])
        result = []
        for i in range(k, len(nums)+1):
            if k % 2 == 0:
                result.append((window[k//2] + window[k//2 - 1]) / 2)
            else:
                result.append(window[k//2])
            if i == len(nums):
                break
            window.remove(nums[i-k])
            bisect.insort(window, nums[i])
        return result