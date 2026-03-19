class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
            res = max(res, left + right)
            return max(left, right) #选择一边供父节点延伸的最长路径
        dfs(root)
        return res

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left_path, right_path = 0, 0
            if node.left and node.left.val == node.val:
                left_path = left + 1
            if node.right and node.right.val == node.val:
                right_path = right + 1
            res = max(res, left_path + right_path)
            return max(left_path, right_path) #选择一边供父节点延伸的最长路径
        dfs(root)
        return res