class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g, labelCt, ans = defaultdict(list), defaultdict(int), [0] * n
        
        for a, b in edges:                              #  <-- 1     
            g[a].append(b)
            g[b].append(a)
        
        def dfs(node=0, par=None):                      #  <-- 2
            prev = labelCt[labels[node]]
            labelCt[labels[node]] += 1
            
            for child in g[node]:
                if child != par: dfs(child, node)

            ans[node] = labelCt[labels[node]] - prev    # <-- 3

        dfs()
        return ans   