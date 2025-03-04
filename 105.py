# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def bulid(preorder, inorder):
            if not preorder:
                return
            root_val = preorder[0]
            root = TreeNode(root_val)
            root_index = inorder.index(root_val)
            inorder_left = inorder[:root_index]
            inorder_right = inorder[root_index+1:]
            pre_left = preorder[1:len(inorder_left)]
            pre_right = preorder[len(inorder_left):]
            root.left = bulid(pre_left, inorder_left)
            root.right = bulid(pre_right, inorder_right)
            return root
        root = bulid(preorder, inorder)
        return root