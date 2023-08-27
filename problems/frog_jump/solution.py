class Solution:
    def canCross(self, stones: List[int]) -> bool:
        a = set(stones)
        if stones[1]!= 1:
            return False

        @cache
        def dfs(last,pos):
            if pos == stones[-1]:
                return True
            if last == pos:
                return False
            jump = pos - last
            for x in [pos + jump - 1, pos + jump, pos + jump + 1]:
                if x in a:
                    if dfs(pos, x):
                        return True
            return False
        
        return dfs(0, 1)
