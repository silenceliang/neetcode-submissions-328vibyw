# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def diameter(root):
            if root:
                return max(diameter(root.left), diameter(root.right))+1
            return 0
        
        left = diameter(root.left)
        right = diameter(root.right)

        return max(left+right, 
        self.diameterOfBinaryTree(root.left), 
        self.diameterOfBinaryTree(root.right))