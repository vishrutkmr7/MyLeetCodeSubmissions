class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums:
            return [f"{lower}->{upper}"] if lower != upper else [f"{lower}"]
        result = []
        if lower < nums[0]:
            result.append(
                f"{lower}->{nums[0] - 1}" if lower != nums[0] - 1 else f"{lower}"
            )
        result.extend(
            f"{nums[i] + 1}->{nums[i + 1] - 1}"
            if nums[i] + 1 != nums[i + 1] - 1
            else f"{nums[i] + 1}"
            for i in range(len(nums) - 1)
            if nums[i] + 1 < nums[i + 1]
        )
        if nums[-1] < upper:
            result.append(
                f"{nums[-1] + 1}->{upper}"
                if nums[-1] + 1 != upper
                else f"{nums[-1] + 1}"
            )
        return result
