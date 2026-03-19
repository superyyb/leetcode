#纯函数式
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        #找到所有路径产生的numbers，计算其总和
        def getPaths(root: Optional[TreeNode]) -> list:
            if not root:
                return []
            if not root.left and not root.right:
                return [[root.val]]
            paths = []
            for path in getPaths(root.left):
                paths.append([root.val] + path)
            for path in getPaths(root.right):
                paths.append([root.val] + path)
            return paths
        all_paths = getPaths(root)
        total = 0
        for path in all_paths:
            num = 0
            for d in path:
                num = num * 10 + d
            total += num
        return total

#函数式 直接累加数值
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], curr: int) -> int:
            if not node:
                return 0
            curr = curr * 10 + node.val
            # 到了叶子：curr 就是这一条路的完整数字
            if not node.left and not node.right:
                return curr
            # 否则继续累加左右子树的结果
            return dfs(node.left,  curr) + dfs(node.right, curr)
        return dfs(root, 0)

#累加器
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(node, curr):
            nonlocal total
            if not node:
                return
            # 把当前节点的值拼到末尾
            curr = curr * 10 + node.val
            # 遇到叶子，就把这条路径对应的数字累加到 total
            if not node.left and not node.right:
                total += curr
                return #这里的return就是直接跳出本层 dfs，不用继续往下了
            dfs(node.left, curr)# 否则继续往下
            dfs(node.right, curr)
        dfs(root, 0)
        return total