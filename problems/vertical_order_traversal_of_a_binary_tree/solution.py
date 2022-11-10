# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq as hq


class Solution:
        
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        heap = []
        hq.heapify(heap)

        def dfs(root, depth, position):
            if not root:
                return
            hq.heappush(heap, (position, depth, root.val))
            dfs(root.left, depth + 1, position - 1)
            dfs(root.right, depth + 1, position + 1)

        dfs(root, 0, 0)
        result = []
        posHold = -float("inf")
        arrayHold = []
        while heap:
            pos, depth, val = hq.heappop(heap)
            # print((pos, depth, val))
            if pos != posHold:
                if len(arrayHold) > 0:
                    result.append(arrayHold)
                    arrayHold = []
                posHold = pos
            arrayHold.append(val)
        result.append(arrayHold)
        return result