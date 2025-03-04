# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def bulid(inorder, postorder):
            if not inorder:
                return
            root_val = postorder[-1]
            root_index = inorder.index(root_val)
            root = TreeNode(root_val)
            in_lefttree = inorder[:root_index]
            in_righttree = inorder[root_index+1:]
            post_lefttree = postorder[:len(in_lefttree)]
            post_righttree = postorder[len(in_lefttree):-1]
            root.left = bulid(in_lefttree, post_lefttree)
            root.right = bulid(in_righttree, post_righttree)
            return root
        root = bulid(inorder, postorder)
        return root