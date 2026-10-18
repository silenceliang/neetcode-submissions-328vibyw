# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        N = len(inorder)
        # inorder map: val -> idx
        inorder_map = {inorder[i]:i for i in range(N)}

        # preorder idx
        def dfs(idx, left, right):
            if left > right:
                return None
            val = preorder[idx]
            root = TreeNode(val)
            inorder_idx = inorder_map[val]
            left_size = inorder_idx - left
            root.left = dfs(idx+1, left, inorder_idx-1)
            root.right = dfs(idx+1+left_size, inorder_idx+1, right)
            return root

        return dfs(0, 0, N-1)