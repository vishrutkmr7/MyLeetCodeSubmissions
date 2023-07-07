class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        maxf = res = 0
        count = Counter()
        for i in range(len(answerKey)):
            count[answerKey[i]] += 1
            maxf = max(maxf, count[answerKey[i]])
            if res - maxf < k:
                res += 1
            else:
                count[answerKey[i - res]] -= 1
        return res