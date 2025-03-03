# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False
        stack = [p,q]
        while stack:
            tree1 = stack.pop()
            tree2 = stack.pop()
            if tree1.val != tree2.val:
                return False
            if (tree1.left and not tree2.left) or (not tree1.left and tree2.left):
                return False
            if tree1.left and tree2.left:
                stack.append(tree1.left)
                stack.append(tree2.left)
            if (tree1.right and not tree2.right) or (not tree1.right and tree2.right):
                return False
            if tree1.right and tree2.right:
                stack.append(tree1.right)
                stack.append(tree2.right)
        return True