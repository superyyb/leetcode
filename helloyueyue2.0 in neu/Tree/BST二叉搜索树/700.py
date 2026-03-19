from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:#recursion #“⚠️只要递归的目的是返回值，就必须 return 递归调用。”
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #node logic:
        #node.val < val -> node.right
        #node.val == val -> node
        #node.val > val -> node.left
        if not root:
            return None
        if root.val==val:
            return root
        elif root.val<val:
            return self.searchBST(root.right,val)#别漏了return
        else:
            return self.searchBST(root.left,val)

#simplify
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        return self.searchBST(root.left, val) or self.searchBST(root.right, val)

class Solution:#recursion with helper function
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(root):
            if not root or val == root.val:
                return root
            left = dfs(root.left)
            right = dfs(root.right)
            if val > root.val:
                return right
            if val < root.val:
                return left
        return dfs(root)

class Solution:#BFS
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        queue=deque([root])
        res=[]
        while queue:
            cur=queue.popleft()
            if cur.val==val:
                return cur
            elif cur.val>val:
                if cur.left:
                    queue.append(cur.left)
            elif cur.val<val:
                if cur.right:
                    queue.append(cur.right)

sol=Solution()
root = [4,2,7,1,3]
val = 5
res=sol.searchBST(root,val)