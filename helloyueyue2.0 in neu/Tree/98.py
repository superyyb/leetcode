#rule:for a node, tree.left<tree.val tree.right>tree.val
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #node logic:
    #如果当前节点为空：这条路径是合法的，返回 True。
    #如果当前节点值不在 (low, high) 之间：违反 BST 定义，返回 False。
    #否则：继续递归检查左右子树，并且更新它们各自的上下界。
        def dfs(root, low, high) -> bool:
            if not root:
                return True
            if not (low < root.val < high):
                return False
            return dfs(root.left, low, root.val) and dfs(root.right, root.val, high)
        return dfs(root, float('-inf'), float('inf'))
'''
❌解：
def dfs(root, low, high) -> bool:
    if not root:
        return True
    if (low < root.val < high):
        return True#一旦这里return True 永远不会进入递归
    else:
        return dfs(root.left, low, root.val) and dfs(root.right, root.val, high)
'''

#❌错误解法
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, low, high):
            if not root:
                return True
            if not (low < root.val < high):
                return False
            return dfs(root.left, low, root.val) and dfs(root.right, root.val, high)
        if dfs(root, float("-inf"), float("inf")):
            return True
        return self.isValidBST(root.left) and self.isValidBST(root.right)
"""
❌在这道题和572 Is subTree 不一样
1.isSubtree 是局部匹配。对子树你可以在整棵树里“到处试根”，因为是否相等只取决于这两个子树本身；
2.isValidBST 需要祖先给下来的上下界。你在主函数里换根重启检查，会把这些上下界丢掉，
于是会把“局部看着都对、但放回原树就不对”的情况判成 True。
"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode],low=float('-inf'),high=float('inf')) -> bool:
        if root is None:
            return True
        stack=[(root,low,high)]
        while stack:
            root, low_val, high_val=stack.pop()
            if root is None:
                continue
            if not (low_val<root.val<high_val):
                return False
            stack.append((root.left,low_val,root.val))
            stack.append((root.right,root.val,high_val))
        return True

if __name__ == "__main__":
    # Construct a simple BST:
    #        5
    #       / \
    #      3   7
    #     / \   \
    #    2   4   8
    root = TreeNode(5,
                    TreeNode(3, TreeNode(2), TreeNode(4)),
                    TreeNode(7, None, TreeNode(8)))
    sol = Solution()
    print(sol.isValidBST(root))
