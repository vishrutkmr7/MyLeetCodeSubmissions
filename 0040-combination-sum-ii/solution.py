class Solution:
    def combinationSum2(self, numbers: List[int], target: int) -> List[List[int]]:
        numbers.sort()
        result = []
        self.backtrack(numbers, target, 0, [], result)
        return result

    def backtrack(
        self,
        numbers: list[int],
        target: int,
        index: int,
        path: list[int],
        result: list[list[int]],
    ):
        if target == 0:
            result.append(path)
            return

        for i in range(index, len(numbers)):
            if i > index and numbers[i] == numbers[i - 1]:
                continue

            if numbers[i] > target:
                break

            self.backtrack(
                numbers, target - numbers[i], i + 1, path + [numbers[i]], result
            )
