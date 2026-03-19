class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
#postorder:left-right-root

class Solution:#recursion
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res=[]
        def post(root):
            for child in root.children:
                post(child)
            res.append(root.val)
        post(root)
        return res

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack=[root]
        res=[]
        while stack:
            cur=stack.pop()
            res.append(cur.val)
            if cur.children:
                for child in cur.children:
                    stack.append(child)
        return res[::-1]