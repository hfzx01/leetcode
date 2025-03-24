# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            if not node:
                return 0
            left = dfs(node.left, depth)
            right = dfs(node.right, depth)
            dia = left + right
            if dia > self.diameter:
                self.diameter = dia
            return 1 + max(left, right)
        dfs(root, 0)
        return self.diameter
