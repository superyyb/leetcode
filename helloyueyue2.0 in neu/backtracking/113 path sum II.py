# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#backtrack（共享 path，需要 pop）
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        #backtracking
        #如果叶子节点并且满足target 加入到res
        res = []
        if not root:
            return []
        path = [] #⚠️思考：为什么path不用nonlocal
        def dfs(root, curr_sum):
            if not root:
                return
            curr_sum += root.val
            path.append(root.val)
            if not root.left and not root.right:
                if targetSum == curr_sum:
                    res.append(path[:])
            dfs(root.left, curr_sum)
            dfs(root.right, curr_sum)
            path.pop()
        dfs(root, 0)
        return res


#backtrack 隐式（不共享 path，不需要 pop）
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return res
        def dfs(root, path):
            if not root:
                return
            if not root.left and not root.right:
                if sum(path) == targetSum:
                    res.append(path)
                    return #记得直接return，叶子没有子节点再下探了
            if root.left:
                dfs(root.left, path + [root.left.val])#每次递归传的是一个新 list
            if root.right:
                dfs(root.right, path + [root.right.val])
        dfs(root, [root.val])
        return res


#BFS
from collections import deque
from typing import Optional
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        #BFS queue((root,total,path))
        res=[]
        if not root:
            return []#base case
        queue=deque([(root,root.val,[root.val])])
        while queue:
            cur,total,path=queue.popleft()
            if not cur.left and not cur.right:
                if total==targetSum:
                    res.append(path)
            if cur.left:
                queue.append((cur.left,total+cur.left.val,path+[cur.left.val]))
            if cur.right:
                queue.append((cur.right,total+cur.right.val,path+[cur.right.val]))
        return res