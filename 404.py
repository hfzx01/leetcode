# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            result = 0
            if node is None:
                return 0
            if node.left and not node.left.left and not node.left.right:
                result += node.left.val
            result += dfs(node.left)
            result += dfs(node.right)
            return result
        result = dfs(root)
        return result
