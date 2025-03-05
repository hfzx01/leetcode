# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = None
        self.min_ = float('inf')
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        self.getMinimumDifference(root.left)
        if self.pre and abs(self.pre.val - root.val) < self.min_:
            self.min_ = abs(self.pre.val - root.val)
        self.pre = root
        self.getMinimumDifference(root.right)
        return self.min_