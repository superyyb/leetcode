class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # 节点逻辑：
        # update the max_val and min_val of a path
        # 叶子节点逻辑：
        # update max_diff
        max_diff = 0
        if not root:
            return 0
        def dfs(root, min_val, max_val):
            nonlocal max_diff
            if not root:
                return
            if root.val < min_val:
                min_val = root.val
            elif root.val > max_val:
                max_val = root.val
            if not root.left and not root.right:
                max_diff = max(max_diff, max_val - min_val)
            dfs(root.left, min_val, max_val)
            dfs(root.right, min_val, max_val)
        dfs(root, root.val, root.val)
        return max_diff


#函数式
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, max_val, min_val):
            if not root:
                return max_val - min_val  #在叶子或空节点时，返回这一路径的最大差值
            max_val = max(max_val, root.val)
            min_val = min(min_val, root.val)
            left = dfs(root.left, max_val, min_val) #分别左右两树遍历
            right = dfs(root.right, max_val, min_val)
            return max(left, right)
        return dfs(root, root.val, root.val)