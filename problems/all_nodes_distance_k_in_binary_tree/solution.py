# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        conn = defaultdict(list)
        
        def connect(parent, child):
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)

            if child.left:
                connect(child, child.left)

            if child.right:
                connect(child, child.right)

        connect(None, root)
        bfs = [target.val]
        seen = set(bfs)

        for i in range(k):
            new_level = []
            for node in bfs:
                for conn_node in conn[node]:
                    if conn_node not in seen:
                        new_level.append(conn_node)
            
            bfs = new_level
            seen |= set(bfs)

        return bfs