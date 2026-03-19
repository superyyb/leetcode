class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        不仅需要记录depth，还需要记录LCA
        记录不一定要列为参数，直接返回tuple也可以
        """
        def dfs(root):
            if not root:
                return (None, 0)
            left_LCA, left_depth = dfs(root.left)
            right_LCA, right_depth = dfs(root.right)
            if left_depth == right_depth:
                return (root, left_depth + 1)
            if left_depth > right_depth:
                return (left_LCA, left_depth + 1)
            if left_depth < right_depth:
                return (right_LCA, right_depth + 1)
        lca, depth = dfs(root) #tuple unpacking
        return lca