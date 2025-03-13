# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def rec(node):
            if not node:
                return (0, 0)
            left = rec(node.left)
            right = rec(node.right)
            val1 = node.val + left[0] + right[0]
            val2 = max(left[0], left[1]) + max(right[0], right[1])
            return (val2, val1)
        return max(rec(root))
