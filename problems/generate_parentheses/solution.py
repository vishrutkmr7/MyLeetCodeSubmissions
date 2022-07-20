class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(path, left, right):
            if left > n or right > n:
                return

            if left == right == n:
                res.append(path)
                return

            if left > right:
                dfs(f"{path}(", left + 1, right)
                dfs(f"{path})", left, right + 1)

            else:
                dfs(f"{path}(", left + 1, right)

        dfs("", 0, 0)
        return res
