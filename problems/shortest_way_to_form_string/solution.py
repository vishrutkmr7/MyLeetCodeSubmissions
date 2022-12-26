class Solution:
    def shortestWay(self, source: str, target: str) -> int:

        def inc():
            self.cnt += 1
            return 0

        self.cnt = i = 0
        for t in target:
            i = source.find(t, i) + 1 or source.find(t, inc()) + 1
            if not i:
                return -1
        return self.cnt + 1