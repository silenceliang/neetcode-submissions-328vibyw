# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs
        # check node val more than root
        def good(root, maxVal):
            if not root:
                return 0
            count = 1 if root.val >= maxVal else 0
            maxVal = max(maxVal, root.val)
            return count + good(root.left, maxVal) + good(root.right, maxVal)
        
        return good(root, root.val)