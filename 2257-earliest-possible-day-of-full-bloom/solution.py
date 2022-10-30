class Solution:
    def earliestFullBloom(self, plantTime: list[int], growTime: list[int]) -> int:

        min_time = acc_plant = 0

        for grow, cur_plant in reversed(sorted(zip(growTime, plantTime))):
            acc_plant += cur_plant
            min_time = max(min_time, acc_plant + grow)

        return min_time
