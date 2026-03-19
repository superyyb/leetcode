# Definition for a binary tree node.
from typing import Optional
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
    1.先定义sameTree函数（判断两棵树是否完全一样）
    2.再运行isSubtree函数（在整棵大树里到处找是否有sameTree）
        2.1 定义返回条件 if dfs(root, subRoot): return True 检查当前节点。
        2.2 递归整个树self.isSubtree(root.left, subRoot) 和 self.isSubtree(root.right, subRoot)
        """
        if not root:
            return False
        def dfs(p:TreeNode,q:TreeNode):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            return dfs(p.left,q.left) and dfs(p.right,q.right)
        if dfs(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

