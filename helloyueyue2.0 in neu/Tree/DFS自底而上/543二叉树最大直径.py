#直径由左右两子树节点相加再减1而成
#先用分治 Bottom-Up计算左右子树高度，再计算diameter = max(max_diameter, left + right)。
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #节点逻辑：
        #return 自己 + max(left, right) 给上一级
        #更新max_diameter为left+right
        max_diameter = 0
        def CalHeight(root):
            nonlocal max_diameter
            if not root:
                return 0
            left_h = CalHeight(root.left)
            right_h = CalHeight(root.right)
            max_diameter = max(max_diameter, left_h + right_h)
            return 1 + max(left_h, right_h)
        CalHeight(root)
        return max_diameter
    '''
为什么这道题一定需要helper function
LeetCode 要求这个函数最终 return 的值是直径。但递归过程里你需要 return 的是“高度”
diameter 的计算需要两种“返回”：
✔ 1. 返回高度（给父节点继续）
✔ 2. 记录全局最大直径（不返回给父节点，而是全局结果）
    '''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #当前节点逻辑
        #找到并更新max_diameter = left+right
        #return max(left, right)+1提供自己的高度给上一级
        self.max_diameter = 0
        def dfs(node):
            if not node:
                return 0
            left_h = dfs(node.left)
            right_h = dfs(node.right)
            # 更新最大直径：左高 + 右高
            self.max_diameter = max(self.max_diameter, left_h + right_h)
            # 返回当前节点高度：1 + max(左右子树高度)
            return 1 + max(left_h, right_h)
        dfs(root)
        return self.max_diameter