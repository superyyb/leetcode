class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
    不知道 p、q 在左边还是右边，只能全树搜一遍。
    对于每个节点，我需要打听：
        左子树有没有看到 p 或 q？
        右子树有没有看到 p 或 q？
        自己是不是 p 或 q
        '''
        #node logic:
        #p, q in left: LCA in left
        #p, q in right: LCA in right
        #p, q in left and right: LCA == root
        if root == p or root == q or root is None:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif left and not right:
            return left
        else:
            return right

class Solution:  # recursion O(n) O(h)H 为树高（最坏 O(N)）。
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q or root is None:  # 自己是不是p/q
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is not None and right is not None:
            # 如果左右子树都找到了一个目标节点，说明当前节点是最近公共祖先
            return root
        if left is not None and right is None:
            # 如果只有左子树找到了，说明两个目标节点都在左边
            return left
        if left is None and right is not None:
            # 如果只有右子树找到了，说明两个目标节点都在右边
            return right





