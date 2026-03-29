#rule:for a node, tree.left<tree.val tree.right>tree.val
'''
1. 函数语义：
判断以 node 为根的子树，是否所有节点都在 (min_val, max_val) 范围内

2. 当前节点：
检查 node.val 是否在 (min_val, max_val) 范围内
不在 → 直接返回 False

3. 往下传什么 / 从下面收什么？
往下传：
  走左边 → 把 node.val 作为新的上界传下去
  走右边 → 把 node.val 作为新的下界传下去

从下面收：
  左右子树各返回一个 True/False
  两个都是 True 才返回 True

4. base case：什么时候停止？
node 为空 → 说明走到底了，没有违规，返回 True

'''

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
        def dfs(node, min_val, max_val):
            if not node:  # 答案4：base case
                return True
            if not (min_val < node.val < max_val):  # 答案2：当前节点处理
                return False
            return (dfs(node.left, min_val, node.val) and  # 答案3：往下传
                    dfs(node.right, node.val, max_val))  # 答案1的体现
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
