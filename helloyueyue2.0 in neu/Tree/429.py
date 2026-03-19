"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res=[]
        if not root:
            return []
        queue=deque([root])
        while queue:
            level=[]
            for i in range(len(queue)):
                cur=queue.popleft()
                level.append(cur.val)
                if cur.children:
                    for child in cur.children:
                        queue.append(child)
            res.append(level)
        return res
