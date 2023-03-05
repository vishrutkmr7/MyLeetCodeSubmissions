class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        # create a dict of value: index
        d = {}
        for i, v in enumerate(arr):
            if v not in d:
                d[v] = [i]
            else:
                d[v].append(i)
        # BFS
        q = [0]
        visited = {0}
        step = 0
        while q:
            step += 1
            for _ in range(len(q)):
                i = q.pop(0)
                # check left
                if i >= 1 and i - 1 not in visited:
                    if i - 1 == n - 1:
                        return step
                    q.append(i - 1)
                    visited.add(i - 1)
                # check right
                if i + 1 < n and i + 1 not in visited:
                    if i + 1 == n - 1:
                        return step
                    q.append(i + 1)
                    visited.add(i + 1)
                # check same value
                if arr[i] in d:
                    for j in d[arr[i]]:
                        if j not in visited:
                            if j == n - 1:
                                return step
                            q.append(j)
                            visited.add(j)
                    del d[arr[i]]
        return -1
