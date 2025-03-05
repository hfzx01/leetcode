# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left and root.right:
                cur = root.right
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                return root.right
            elif root.left and not root.right:
                return root.left
            elif not root.left and root.right:
                return root.right
            else:
                return None
        return root

