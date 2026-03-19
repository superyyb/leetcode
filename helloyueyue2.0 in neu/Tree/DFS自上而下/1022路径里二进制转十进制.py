#累加器
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total = 0
        paths = []
        def dfs(root, path):
            nonlocal total
            if not root:
                return
            path += str(root.val)
            if not root.left and not root.right:
                paths.append(path)
            dfs(root.left, path)
            dfs(root.right, path)
        dfs(root, "")
        for path in paths:#["100", "101", "110", "111"]
            n = len(path)
            dight = 0
            for i in range(n):
                dight += int(path[i]) * (2 ** (n - i - 1))
            total += dight
        return total

#函数式 直接在dfs里相加
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr):
            if not node:
                return 0
            curr = curr * 2 + node.val#经典二进制构造算法
            if not node.left and not node.right:
                return curr
            return dfs(node.left, curr) + dfs(node.right, curr)
        return dfs(root, 0)

    """
    十进制转二进制
    def to_binary(n):
        if n == 0:
            return "0"
        res = ""
        while n > 0:
            res = str(n % 2) + res
            n = n // 2
    return res
    
    13 ÷ 2 = 6 ... 1   ← 最低位
    6 ÷ 2  = 3 ... 0
    3 ÷ 2  = 1 ... 1
    1 ÷ 2  = 0 ... 1   ← 最高位
    13: 1101
    """