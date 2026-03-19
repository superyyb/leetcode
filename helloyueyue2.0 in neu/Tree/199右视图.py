# Definition for a binary tree node.
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#bottom up
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #单个节点逻辑：return root.val + merge(left,right)
        #len(left) > len(right) : right + left[right:]
        if not root:
            return []
        left = self.rightSideView(root.left)
        right = self.rightSideView(root.right)
        if len(left) > len(right):
            return [root.val] + right + left[len(right):]
        else:
            return [root.val] + right

#iteration
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # list all the rightmost node in a level
        # leverorder queue/BST
        if not root:
            return []  # base case
        res = []
        queue = deque([root])
        while queue:
            for i in range(len(queue)):  # i:index of nodes in every level
                cur = queue.popleft()
                if i == len(queue) - 1:
                    res.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return res
#不用上面这么麻烦
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            for i in range(len(queue)):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(curr.val)#每次for loop里最后一个curr就是我们要的最右边的节点
        return res

#recursion累加器
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #return the list of rightmost node.vals
        """
        先递归右子树，再左:
        对于每一层，最先被访问到的必定是“最右侧”的那个节点。
        """
        res = []
        def recursion(root, depth = 0):
            if not root:
                return
            if depth == len(res):#第一次到达这一层时
                res.append(root.val)
            recursion(root.right, depth + 1)
            recursion(root.left, depth + 1)
        recursion(root)
        return res

