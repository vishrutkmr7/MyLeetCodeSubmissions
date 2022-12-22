class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lucky_numbers = []
        for item in matrix:
            lucky_numbers.extend(
                item[column]
                for column in range(len(item))
                if item[column] == min(item)
                and item[column] == max(matrix[i][column] for i in range(len(matrix)))
            )
        return lucky_numbers
