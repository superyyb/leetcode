# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    返回值
    1.递归函数自己返回一个列表，且对空节点要 return []，对叶子节点 return [val]。
	2.用它就别靠外部变量。
    """
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaflist(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            left_list = leaflist(root.left)
            right_list = leaflist(root.right)
            return left_list + right_list
            #中间节点并不自己 append(node.val)，而是负责“组合”它左右两边递归的返回值
        return leaflist(root1) == leaflist(root2)

class Solution:
    """
    累加器:
    1.外部 res=[]，内部不返回值，直接 res.append(...)。
	2.用它就别再想 return 要拿到什么。
    """
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaflist(root,res):
            if not root:
                return
            if not root.left and not root.right:
                res.append(root.val)
            else:
                leaflist(root.left, res)
                leaflist(root.right, res)
        leaves1, leaves2 = [], []
        leaflist(root1, leaves1)
        leaflist(root2, leaves2)
        return leaves1 == leaves2