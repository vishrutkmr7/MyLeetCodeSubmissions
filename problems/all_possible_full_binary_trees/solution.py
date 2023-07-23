# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def clone(self, tree: TreeNode) -> TreeNode:
        if not tree:
            return None
        new_tree = TreeNode(0)
        new_tree.left = self.clone(tree.left)
        new_tree.right = self.clone(tree.right)
        return new_tree

    def allPossibleFBT(self, N: int) -> List[Optional[TreeNode]]:
        if N % 2 == 0:
            return []
        if N == 1:
            return [TreeNode(0)]
    
   
        cache = [[TreeNode(0)]]
        for root in range(1, N // 2):
            cache.append([])
            for left_size in range(root):
                for left in cache[left_size]:
                    for right in cache[root - left_size - 1]:
                        new_tree = TreeNode(0)
                        new_tree.left = left
                        new_tree.right = right
                        cache[-1].append(new_tree)
  
        ret = []
        for root in range(N // 2):
            for left in cache[root]:
                for right in cache[N // 2 - root - 1]:
                    new_tree = TreeNode(0)
                    new_tree.left = self.clone(left)
                    new_tree.right = self.clone(right)
                    ret.append(new_tree)
        
        return ret