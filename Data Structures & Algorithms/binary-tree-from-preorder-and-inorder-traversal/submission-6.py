class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. 建立雜湊表，O(1) 查詢 inorder 中的索引
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        # preorder idx, inorder left ptr, inorder right ptr
        def helper(pre_idx: int, left: int, right: int) -> Optional[TreeNode]:
            # 若範圍無效，返回 None
            if left > right:
                return None
            
            # 2. 建立當前根節點
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            
            # 3. 取得根節點在 inorder 中的位置，並計算左子樹大小
            idx = inorder_map[root_val]
            left_size = idx - left
            
            # 4. 遞迴建構左右子樹
            # 左子樹在 preorder 的起始位置是 pre_idx + 1
            root.left = helper(pre_idx + 1, left, idx - 1)
            
            # 右子樹在 preorder 的起始位置是 pre_idx + 1 + 左子樹大小
            root.right = helper(pre_idx + 1 + left_size, idx + 1, right)
            
            return root

        return helper(0, 0, len(inorder) - 1)