class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Using Walrus operator
        return len(c := Counter(arr)) == len(set(c.values()))