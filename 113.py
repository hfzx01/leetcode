# Definition for a binary tree node.
from copy import deepcopy
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        res = [root.val]
        def dfs(node, target):

            if not node.left and not node.right and target == 0:
                result.append(res.copy())
                return
            if not node.left and not node.right:
                return
            if node.left:
                res.append(node.left.val)
                dfs(node.left, target - node.left.val)
                res.pop()
            if node.right:
                res.append(node.right.val)
                dfs(node.right, target - node.right.val)
                res.pop()
        dfs(root, targetSum - root.val)
        return result


node7 = TreeNode(7)
node2 = TreeNode(2)
node5 = TreeNode(5)
node1 = TreeNode(1)
node11 = TreeNode(11, node7, node2)
node13 = TreeNode(13)
node4 = TreeNode(4, node5, node1)
node41 = TreeNode(4, node11, None)
node8 = TreeNode(8, node13, node4)
node5 = TreeNode(5, node41, node8)
print(Solution().pathSum(node5, 22))
