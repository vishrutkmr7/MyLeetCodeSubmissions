class Solution:
    def combinationSum(self, numbers: List[int], target: int) -> List[List[int]]:
            res = []

            def dfs(i, cur, total):
                if total == target:
                    res.append(cur.copy())
                    return
                if i >= len(numbers) or total > target:
                    return

                cur.append(numbers[i])
                dfs(i, cur, total + numbers[i])
                cur.pop()
                dfs(i + 1, cur, total)

            dfs(0, [], 0)
            return res
