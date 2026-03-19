# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue=deque([root])
        res=[]
        while queue:
            cur=queue.popleft()
            res.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return len(res)

from collections import deque
class Solution:#直接记录节点个数，不需要另创建一个序列Better One
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue=deque([root])
        count=0
        while queue:
            cur=queue.popleft()
            count+=1#在每次pop出去的时候count+1
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return count

#累加器 带count参数
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(root, count):
            if not root:
                return count
            count += 1
            count = dfs(root.left, count)
            count = dfs(root.right, count)
            return count
        return dfs(root, 0)

#累加器 不带count参数
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def dfs(root):
            if not root:
                return 0
            self.count += 1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.count
"""
为什么这个累加器可以不用传count进入递归函数（区别于104，111）
maxDepth 需要传 height
	•	你用的是 自上而下（top‑down）累加器：height 表示“当前路径的层数”。
	•	这个值因路径不同而不同，必须作为参数沿着递归分支独立传递
countNodes 可以不传 count
	•	这里的count是全局累加，与具体哪条路径无关；只要“访问到一个节点就 +1”。
	•	因为它不依赖“当前递归分支的上下文”，所以不必作为参数传来传去；直接用外部状态记录即可：
"""

#分治 bottom up
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            return left + right + 1
        return dfs(root)
    """
    +1:
    每个非空节点在返回结果时，在返回时都会贡献一个 1（代表自己）。
    所以最终结果就是“递归经过了多少个非空节点，就加了多少个 1”
    这就是分治和累加器的不同之处，不需要在递归过程中计算，而是在每次返回值的时候加1
    """
