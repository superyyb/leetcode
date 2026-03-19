#累加器
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        seen = set()
        def dfs(root):
            if not root:
                return True
            seen.add(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return len(seen) == 1

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, val):
            if not node:
                return True
            if node.val != val:#函数式：先把判断基准列出来
                return False
            left_ok = dfs(node.left, val) #再分别递归，判断左右是否符合基准
            right_ok = dfs(node.right, val)
            return left_ok and right_ok
        return dfs(root, root.val)