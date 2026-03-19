class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0
        def dfs(root):
            nonlocal res
        #python多值返回：
        #在 return 后写多个逗号分隔的表达式，自动打包成元组返回
            if not root:
                return 0, 0
            left_sum, left_count = dfs(root.left)
            right_sum, right_count = dfs(root.right)
            curr_sum = root.val + left_sum + right_sum
            curr_count = 1 + left_count + right_count#计节点个数
            if curr_sum // curr_count == root.val:
                res += 1
            return curr_sum, curr_count
        dfs(root)
        return res