class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
from collections import deque
class Solution:#BFS/queue
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        queue=deque([(root,1)])
        while queue:
            cur,depth=queue.popleft()
            if cur.children:
                for child in cur.children:
                    queue.append((child,depth+1))
        return depth

class Solution:#recursion，postorder:left right root
    def postorder(self,root):
        if not root:
            return 0
        max_depth=0
        for child in root.children:
            depth=self.postorder(child)
            max_depth=max(max_depth,depth) #renew value of max_depth everytime
        return max_depth+1
        #后序就是要处理完所有children之后再计算当前节点的贡献（+1）
    def maxDepth(self, root: 'Node') -> int:
        return self.postorder(root)