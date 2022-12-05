class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_nums = sorted(score, reverse=True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        return [
            medals[i] if i < 3 else str(i + 1)
            for i in [sorted_nums.index(num) for num in score]
        ]