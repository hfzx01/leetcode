# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur:
                    level.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    level.append('')
            if cur != root and (len(level) % 2 != 0 or level != level[::-1]):
                return False
        return True