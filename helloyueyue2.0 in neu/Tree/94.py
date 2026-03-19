from typing import List, Optional
class Treenode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def inorderTraversal(self,root:Optional[Treenode])->List[int]:
        # Optional[Treenode]表示root可能是Treenode也可能是None
        res=[]
        def inorder(root):# 每次递归都需要传入一个新的root作为子树的根节点。
            if root is None:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res

#inorder: left root right
class TreeNode:#one function
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def inorderTraversal(self,root)->list[int]:
        res=[]
        if not root:
            return res
        if root.left:
            res+=self.inorderTraversal(root.left)
        res.append(root.val)
        if root.right:
            res+=self.inorderTraversal(root.right)
        return res

#stack
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []
        stack = []
        curr = root
        while curr or stack:#入stack:root-left- 出stack 再入right
            if curr:
                stack.append(curr)#在stack里append节点
                curr = curr.left
            else:
                curr = stack.pop()
                res.append(curr.val)#在stack里append节点的值
                curr = curr.right
        return res

def lower_bound(arr: List[int], target: int) -> int:
    l, r = 0, len(arr)
    while l < r:
        mid = l + (r - l) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid
    if l !=len(arr) and arr[l] == target:
        return l
    return -1


