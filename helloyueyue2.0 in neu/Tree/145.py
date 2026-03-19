# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:#Accumulator
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = [] #外部收集结果
        def postorder(root):
            if not root:
                return #递归函数只“访问”＋“深入”，不返回有用值
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
        postorder(root)
        return res

class Solution:#返回值模式
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        res=[]
        if not root:
            return res
        if root.left:
            res+=self.postorderTraversal(root.left)
        if root.right:
            res+=self.postorderTraversal(root.right)
        res.append(root.val)
        return res

#iteration
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #left-right-root
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)#root先入res
            if curr.left: #先左再压右 → 出栈顺序是先右再左
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return res[::-1]#res:root,right,left反转后得到答案