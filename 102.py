# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []
        def level(node, result):
            if node is None:
                return
            if len(results) == result:
                results.append([])
            results[result].append(node.val)
            level(node.left, result + 1)
            level(node.right, result + 1)
        level(root, 0)
        return results