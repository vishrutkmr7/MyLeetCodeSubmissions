class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        out = []
        queue = deque(range(1, 10))
        while queue:
            elem = queue.popleft()
            if low <= elem <= high:
                out.append(elem)
            last = elem % 10
            if last < 9:
                queue.append(elem * 10 + last + 1)

        return out