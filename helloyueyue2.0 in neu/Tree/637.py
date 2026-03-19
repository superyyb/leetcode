# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional,List
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        queue=[root]
        res=[]
        while queue:
            level=[]
            for i in range(len(queue)):
                cur=queue.pop(0)
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(level)
        aver_res=[]
        for level in res:
            aver_val=sum(level)/len(level)
            aver_res.append(aver_val)
        return aver_res