# Definition for a binary tree node.
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#iteration
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # left leaf: sum+=
        # left node,right node: add to the queue
        left_total = 0
        if not root:
            return 0
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            if cur.left:
                if not cur.left.left and not cur.left.right:
                    left_total += cur.left.val
                else:
                    queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return left_total

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        #up down
        total_sum = 0
        def dfs(root):
            nonlocal total_sum
            if not root:
                return
            if root.left and not root.left.left and not root.left.right:
                total_sum += root.left.val
                return
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return total_sum

#累加器 用列表total = [0] 作为可变容器，内部函数直接 total[0] += …，无需 nonlocal，更简洁
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = [0]  # 用列表来“闭包捕获”累加值
        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            if node.left and not node.left.left and not node.left.right:
                total[0] += node.left.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return total[0]

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        total = 0
        #当前节点逻辑：
        #判断节点的左孩子是否是叶子
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val

        total += self.sumOfLeftLeaves(root.left)
        total += self.sumOfLeftLeaves(root.right)
        return total


