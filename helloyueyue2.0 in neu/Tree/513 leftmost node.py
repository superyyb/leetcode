# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue=deque([root])
        res=0
        while queue:
            for i in range(len(queue)):
                cur=queue.popleft()
                if i==0:
                    res=cur.val #renew the res at the first node in every level
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return res


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue=deque([root])
        res=[]
        while queue:
            level=[]
            for i in range(len(queue)):
                cur=queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(level)
        return res[-1][0]

from collections import deque
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = deque([root])
        node = None
        while queue:
            node = queue.popleft()
            # 先 enqueue 右
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        # 最后一次出队的 node，就是答案
        return node.val