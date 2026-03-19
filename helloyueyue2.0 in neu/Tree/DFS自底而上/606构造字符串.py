class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # 先序遍历：node, left, right
        def dfs(node: Optional[TreeNode]) -> str:
            if not node:
                return ""
            s = str(node.val)
            # 只要右子树存在，或者左子树存在，都需要写左括号
            if node.left or node.right:
                # 左子树可能为空，dfs(None) 返回 ""
                s += "(" + dfs(node.left) + ")"
            # 只有右子树存在时才加
            if node.right:
                s += "(" + dfs(node.right) + ")"
            return s
        return dfs(root)