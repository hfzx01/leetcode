# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def backtracking(node, target):
            if not node:
                return 0
            result = 0
            target += node.val
            if target == targetSum:
                result += 1
            result += backtracking(node.left, target)
            result += backtracking(node.right, target)
            return result
        if not root:
            return 0
        result = backtracking(root, 0)
        result += self.pathSum(root.left, targetSum)
        result += self.pathSum(root.right, targetSum)
        return result