# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        max_product = 0
        total_sum = 0

        def totalSum(root):
            # 节点逻辑：把自己的value和左右孩子的一起return给上一级
            if not root:
                return 0
            left_sum = totalSum(root.left)
            right_sum = totalSum(root.right)
            return root.val + left_sum + right_sum

        def subSum(root):
            # 节点逻辑：
            # 更新max_product
            # return当前值到上一层
            nonlocal max_product
            nonlocal total_sum
            if not root:
                return 0
            left = subSum(root.left)
            right = subSum(root.right)
            subtree = root.val + left + right
            max_product = max(max_product, subtree * (total_sum - subtree))
            return subtree

        total_sum = totalSum(root)
        subSum(root)
        return max_product % (10 ** 9 + 7)
