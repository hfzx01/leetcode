# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 1
        def recursive(node):
            # 0有覆盖，1摄像头，2无覆盖
            if not node:
                return 0
            if not node.left and not node.right:
                return 2
            left = recursive(node.left)
            right = recursive(node.right)
            if left == 2 or right == 2:
                self.result += 1
                return 1
            if left == 1 or right == 1:
                return 0
            if left == 0 and right == 0:
                return 2

        if recursive(root) == 2:
            self.result += 1
        return self.result