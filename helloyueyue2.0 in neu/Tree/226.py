from typing import Optional
#每一层在“子节点都翻好”之后再交换左右。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        queue=[root]
        while queue:
            for i in range(len(queue)):
                cur=queue.pop(0)
                cur.left,cur.right=cur.right,cur.left#只要在弹出每个node的时候加入处理条件即可
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return root

#每次递归调用都会返回一棵「反转好的子树」,
#父节点依赖子递归的返回值，然后用这些返回值去拼接自己的新树结构。
"""
类似于下面求树高
def maxDepth(root):
    if not root:
        return 0
    left = maxDepth(root.left)     # 子问题
    right = maxDepth(root.right)
    return max(left, right) + 1    # 拼结果
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        new_left = self.invertTree(root.left)
        new_right = self.invertTree(root.right)
        root.left, root.right = new_right, new_left
        return root

#递归调用没有利用返回值，只是「顺着树往下走」，在过程中直接修改 root
#不需要返回值
class Solution:#preorder:root-left-right
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)#只是为了递归修改树结构，不关心结果，不要加return
        self.invertTree(root.right)
        return root

class Solution:#postorder:left-right-root
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root

class Solution:#inorder:left-root-right
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.invertTree(root.left)
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        return root


class Solution:#preorder:root-left-right
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        stack=[root]#stack pop order: right-left-root
        while stack:
            cur=stack.pop()
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            cur.left,cur.right=cur.right,cur.left
        return root


if __name__=="__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    sol=Solution()
    result=sol.invertTree(root)
    print(result)