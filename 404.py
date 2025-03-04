# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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


node9 = TreeNode(9)
node15 = TreeNode(15)
node7 = TreeNode(7)
node20 = TreeNode(20, node15, node7)
node3 = TreeNode(3, node9, node20)

print(Solution().sumOfLeftLeaves(node3))
