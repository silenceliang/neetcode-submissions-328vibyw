class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                # 單邊最大延伸值為 0，但子樹最大路徑為負無限大（以防全都是負數）
                return 0, float('-inf')
            
            # 遞迴取得左右子樹的 (單邊最大延伸, 子樹全域最大值)
            left_single, left_max = dfs(node.left)
            right_single, right_max = dfs(node.right)
            
            # 若子樹延伸小於 0，則捨棄不選（視為 0）
            left_single = max(0, left_single)
            right_single = max(0, right_single)
            
            # 1. 經過當前節點的最高路徑總和（左子樹 + 當前節點 + 右子樹）
            through_node = node.val + left_single + right_single
            
            # 2. 目前子樹中的全域最大值
            current_max = max(left_max, right_max, through_node)
            
            # 3. 要回傳給父節點的「單邊最大延伸值」（只能選左或右其中一邊）
            single_path = node.val + max(left_single, right_single)
            
            return single_path, current_max
        
        # 回傳 dfs 結果中的第二個元素（子樹全域最大值）
        return dfs(root)[1]