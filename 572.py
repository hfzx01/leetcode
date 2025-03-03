# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def issame(node1, node2):
            stack1 = [node1, node2]
            while stack1:
                node1 = stack1.pop()
                node2 = stack1.pop()
                if (node1 and not node2) or (not node1 and node2):
                    return False
                if not node1 and not node2:
                    continue
                if node1.val != node2.val:
                    return False
                stack1.append(node1.left)
                stack1.append(node2.left)
                stack1.append(node1.right)
                stack1.append(node2.right)
            return True

        def dfs(node):
            if node is None:
                return False
            if node.val == subRoot.val and issame(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)

        return dfs(root)