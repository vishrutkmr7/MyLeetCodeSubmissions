class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = intermediate = 0
        max_len = 0
        baskets = [-1, -1]

        for right in range(len(fruits)):
            if fruits[right] != baskets[1]:
                if fruits[right] != baskets[0]:
                    left = intermediate
                intermediate = right
                baskets[0], baskets[1] = (
                    baskets[1],
                    fruits[right],
                )
            max_len = max(max_len, right - left + 1)

        return max_len