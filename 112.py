# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, target):
            if not node:
                return False
            if not node.left and not node.right and target == node.val:
                return True

            return dfs(node.left, target - node.val) or dfs(node.right, target - node.val)

        return dfs(root, targetSum)