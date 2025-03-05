# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        def dfs(node, p, q):
            if node is None:
                return
            if node.val <= q.val and node.val >= p.val:
                return node
            left = dfs(node.left, p, q)
            if left:
                return left
            right = dfs(node.right, p, q)
            if right:
                return right

        return dfs(root, p, q)