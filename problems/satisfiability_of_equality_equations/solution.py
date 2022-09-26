class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        s = 0
        for i in equations:
            s = max(s, ord(i[0]) - 97)
            s = max(s, ord(i[3]) - 97)

        parent = []
        rank = []
        for i in range(s + 1):
            parent.append(i)
            rank.append(1)

        def find(x):
            p = parent[x]
            while p != parent[p]:
                p = parent[p]
            parent[x] = p
            return p

        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                if py > px:
                    x, y = y, x
                parent[py] = px
                rank[px] += py

        for i in equations:
            if i[1] == "=":
                union(ord(i[0]) - 97, ord(i[3]) - 97)
        for i in equations:
            if i[1] == "!" and find(ord(i[0]) - 97) == find(ord(i[3]) - 97):
                return False
        return True