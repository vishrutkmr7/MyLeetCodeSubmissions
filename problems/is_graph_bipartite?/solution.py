class Solution:
    def isBipartite(self, arr: List[List[int]]) -> bool:
        def dfs(v,clr,color,arr):

            color[v]=clr

            for i in arr[v]:
                if color[i]==-1:
                    if color[v]==1:
                        if dfs(i,0,color,arr)== False:
                            return False
                    else:
                        if dfs(i,1,color,arr)== False:
                            return False
                elif color[i]==color[v]:
                    return False
            return True

        n=len(arr)
        color=[-1]*n
        for i in range(n):
            if color[i] == -1 and dfs(i, 0, color, arr) == False:
                return 0
        return 1