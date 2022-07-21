class Solution:
    def partition(self, s):
        res = []

        def dfs(i, cur):
            if i == len(s):
                res.append(cur.copy())
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s[i : j + 1]):
                    cur.append(s[i : j + 1])
                    dfs(j + 1, cur)
                    cur.pop()

        dfs(0, [])
        return res

    def isPalindrome(self, s):
        return s == s[::-1]
