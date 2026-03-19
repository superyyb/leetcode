#函数式
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root or not root.left: #如果root为空或者没有子树
            return -1
        if root.left.val > root.val:
            candL = root.left.val
        else:
            candL = self.findSecondMinimumValue(root.left)
        if root.right.val > root.val:
            candR = root.right.val
        else:
            candR = self.findSecondMinimumValue(root.right)
        if candL == -1:
            return candR #子问题的答案通过 candL/candR 接收，再在这一层合并并 return
        if candR == -1:
            return candL
        return min(candL, candR)

"""
要么 用“纯返回值”模式，把左右子树的结果分别收回来再合并——那就参照上面 candL/candR 解法。
要么 用“外部累加器”模式，只维护一个或两个变量，在递归中不停更新它们，参照下面。
"""

#累加器 外部维护变量
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        first = root.val
        second = -1
        def findSecondMin(root):
            nonlocal second
            if not root:
                return
            if second == -1 or root.val < second:
                if root.val > first:
                    second = root.val
            findSecondMin(root.left)
            findSecondMin(root.right)
        findSecondMin(root)
        return second