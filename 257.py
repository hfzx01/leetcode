# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        path = []
        def dfs(node):
            path.append(str(node.val))
            if not node.left and not node.right:
                path1 = '->'.join(path)
                result.append(path1)
            if node.left:
                dfs(node.left)
                path.pop()
            if node.right:
                dfs(node.right)
                path.pop()
        dfs(root)
        return result