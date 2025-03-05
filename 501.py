# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
        self.count = 0
        self.count_max = 0
        self.pre = None
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def find(node):
            if node is None:
                return
            find(node.left)
            if self.pre and node.val == self.pre.val:
                self.count += 1
            else:
                self.count = 1
            if self.count == self.count_max:
                self.result.append(node.val)
            elif self.count > self.count_max:
                self.count_max = self.count
                self.result.clear()
                self.result = [node.val]

            self.pre = node
            find(node.right)
        find(root)
        return self.result


node3 = TreeNode(2)
node2 = TreeNode(2, node3, None)
node1 = TreeNode(1, None, node2)

print(Solution().findMode(node1))