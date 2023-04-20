# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        max_width = 0
        queue = deque([(root, 0)])  # Each tuple contains a TreeNode and its position

        while queue:
            level_length = len(queue)
            leftmost_pos = queue[0][1]  # Position of the leftmost node in the current level
            rightmost_pos = leftmost_pos  # Initialize rightmost_pos with leftmost_pos

            for _ in range(level_length):
                node, pos = queue.popleft()

                # Update rightmost_pos with the position of the current node
                rightmost_pos = pos

                if node.left:
                    queue.append((node.left, pos * 2))
                if node.right:
                    queue.append((node.right, pos * 2 + 1))

            # Update max_width by comparing it with the width of the current level
            max_width = max(max_width, rightmost_pos - leftmost_pos + 1)

        return max_width