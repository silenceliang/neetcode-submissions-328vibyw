# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # find root in the inorder list
        # preorder[0] is root
        if len(preorder) == 0:
            return None
        i = 0
        while i < len(inorder):
            if inorder[i] == preorder[0]:
                break
            i+=1
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        root.right = self.buildTree(preorder[i+1:],  inorder[i+1:])
        return root