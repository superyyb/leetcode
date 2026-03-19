class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #思路：对每一个node要判断是否balanced
        #写一个function判断是否balanced 然后再主函数遍历每个node
        #在 dfs 里做两件事：
        #计算这个节点的高度
        #如果某个子树不平衡，马上返回一个特殊值（比如 -1）来标记“不平衡”
        if not root:
            return True
        def dfs(root) -> int:
            if not root:#空树是平衡的，且高度为0
                return 0
            left_h = dfs(root.left)
            right_h = dfs(root.right)
            if left_h == -1 or right_h == -1:#是否左右子树已经不平衡了
                return -1
            if abs(left_h - right_h) > 1:# 当前节点左右高度差大于 1，也不平衡
                return -1
            return max(left_h + right_h) + 1 # 否则，当前节点是平衡的，返回它的高度
        return dfs(root)

class Solution:#recursion
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_depth(root):#figure out depth of any subtree
            if not root:
                return 0
            left=get_depth(root.left)
            right=get_depth(root.right)
            if left==-1: #剪枝优化：左子树被判定为-1，没必要再计算右子树了
                return -1
            if right==-1: #剪枝优化
                return -1
            if abs(left-right)>1:#核心判断逻辑
                return -1
            return max(left,right)+1 # Postorder:先递归left right 再root+1
        return get_depth(root)!=-1
"""
dfs(node) 的返回值有两种可能：
	1.	>=0 → 子树的高度。
	2.	-1 → 子树不平衡。
	所以不可以在一个函数里既返回bool 又返回int，所以用-1指代不平衡
	 if abs(left-right)>1:
                return False
            return max(left,right)+1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

