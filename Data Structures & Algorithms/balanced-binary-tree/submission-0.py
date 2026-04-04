# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def degree(root):
            if root:
                return 1 + max(degree(root.left), degree(root.right))
            return 0
        if not root:
            return True
        left = degree(root.left)
        right = degree(root.right)

        return abs(left-right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right) 