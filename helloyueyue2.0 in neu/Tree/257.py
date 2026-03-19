class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        #backtracking
        if not root:
            return []
        res = []
        def backtracking(root, s):
            if not root:
                return
            if not root.left and not root.right:
                res.append(s)
                return
            #⚠️在访问 xxx.val 之前，一定要先确认 xxx 不是 None
            if root.left:
                backtracking(root.left, s + '->' + str(root.left.val))
            if root.right:
                backtracking(root.right, s + '->' + str(root.right.val))
        backtracking(root, str(root.val))
        return res


from typing import Optional
from collections import deque
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        #BFS queue=(root,path)
        res=[]#store all paths
        queue=deque([(root,str(root.val))])
        while queue:
            cur,path=queue.popleft()
            if not cur.left and not cur.right:
                res.append(path)
            if cur.left:
                queue.append((cur.left,path+"->"+str(cur.left.val)))
            if cur.right:
                queue.append((cur.right,path+"->"+str(cur.right.val)))
        return res
