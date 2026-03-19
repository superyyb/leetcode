#DFS自底而上
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(root, path):
            if not root:
                return
            if not root.left and not root.right:
                res.append(path)
            if root.left:
                dfs(root.left, path + "->" + str(root.left.val))
            if root.right:
                dfs(root.right, path + "->" + str(root.right.val))
        dfs(root, str(root.val))
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
