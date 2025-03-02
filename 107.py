# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        def up(node, level):
            if node is None:
                return
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            up(node.left, level + 1)
            up(node.right, level + 1)
        up(root, 0)
        return levels[::-1]