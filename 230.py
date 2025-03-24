# 二叉树第k个
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# import heapq
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         result = []
#         def dfs(node, k):
#             if not node:
#                 return
#             heapq.heappush(result, -node.val)
#             if len(result) > k:
#                 heapq.heappop(result)
#             dfs(node.left, k)
#             dfs(node.right, k)
#         dfs(root, k)
#         return - result[0]
# 二叉搜索树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        dfs(root)
        return result[k-1]