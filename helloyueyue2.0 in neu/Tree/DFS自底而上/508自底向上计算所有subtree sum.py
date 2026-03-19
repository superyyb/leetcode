#自底向上：dfs(root.left) 和 dfs(root.right) 都会立即 hit 到空节点分支并各自返回 0。
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        seen = {}
        def dfs(root):
            if not root:
                return 0
            left_sum = dfs(root.left) #先递归到最底层
            right_sum = dfs(root.right)
            total = root.val + left_sum + right_sum#实现一层层往上加
            seen[total] = seen.get(total, 0) + 1
            return total
        dfs(root)
        max_count = max(seen.values())# 找到最高频次
        # 收集所有频次等于 max_count 的子树和
        return [s for s, cnt in seen.items() if cnt == max_count]
        # seen.items:(s, cnt)