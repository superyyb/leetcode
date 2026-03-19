class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        #bottom up
        #节点逻辑
        #total加上 abs(left_sum - right_sum)
        #return root.val +left_sum + right_sum给上一级
        total = 0
        def dfs(node):
            nonlocal total
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val #作为叶子节点，我需要把我的值return给父节点
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            total += abs(left_sum - right_sum)
            return node.val + left_sum + right_sum#父节点需要知道这整棵子树的
        dfs(root)
        return total
        #⚠️dfs 的 return 必须是 “整棵子树的总和”

#❌解：dfs被调用两次
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        #calculate abs diff of left and right
        total = 0
        def dfs(node):
            nonlocal total
            if not node:
                return 0
            if not node.left and not node.right:
                return 0
            total += abs(dfs(node.left) - dfs(node.right))
            return node.val + dfs(node.left) + dfs(node.right)
        dfs(root)
        return total