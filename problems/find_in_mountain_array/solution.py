# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def find_peak_index(self, low, high, mountainArr):
        while low != high:
            mid = low + (high - low) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                low = mid + 1
            else:
                high = mid
        return low

    def binary_search(self, low, high, target, mountainArr, reversed):
        while low != high:
            mid = low + (high - low) // 2
            if reversed:
                if mountainArr.get(mid) > target:
                    low = mid + 1
                else:
                    high = mid
            else:
                if mountainArr.get(mid) < target:
                    low = mid + 1
                else:
                    high = mid
        return low

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()

        peak = self.find_peak_index(1, length - 2, mountain_arr)
        increasing_index = self.binary_search(0, peak, target, mountain_arr, False)
        if mountain_arr.get(increasing_index) == target:
            return increasing_index

        decreasing_index = self.binary_search(peak + 1, length - 1, target, mountain_arr, True)
        if mountain_arr.get(decreasing_index) == target:
            return decreasing_index

        return -1


        