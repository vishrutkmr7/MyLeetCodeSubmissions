class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        deque = collections.deque(tokens)
        ans = bns = 0
        while deque and (power >= deque[0] or bns):
            while deque and power >= deque[0]:
                power -= deque.popleft()
                bns += 1
            ans = max(ans, bns)

            if deque and bns:
                power += deque.pop()
                bns -= 1

        return ans
