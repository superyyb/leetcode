# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

#recursion
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res=[]
        res.append(root.val)
        for child in root.children:
            res.extend(self.preorder(child))
        return res

class Solution:#recursion using helper function
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res=[]
        def dfs(root):
            res.append(root.val)
            for child in root.children:
                dfs(child)
        dfs(root)
        return res

#Preorder:root-left-right
class Solution:#stack
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack=[root]
        res=[]
        while stack:
            cur=stack.pop()#入stack:root,children from right to left
            res.append(cur.val)#出stack:root,left,right
            if cur.children:
                for child in reversed(cur.children):
                    stack.append(child)
        return res
"""
#错解
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res=[]
        stack=[root]
        while stack:
            cur=stack.pop()
            res.append(cur.val)
            for child in cur.children:
                stack.insert(0,child)
        return res
"""