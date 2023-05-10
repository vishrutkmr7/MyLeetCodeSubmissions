class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = defaultdict(int)
        left = 0
        result = 0

        for right, value in enumerate(s):
            hashMap[value] += 1

            while right - left + 1 - max(hashMap.values()) > k:
                hashMap[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result