# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        '''
        Define a function which direction changes every move
        Run the function both left and right to see which one has longest ZigZag path

        single node logic:
        if I come left, then I go right: length + 1, else I go left, reset length
        if I come right, then I go left: length + 1, else I go right, reset length
        '''
        if not root:
            return 0
        max_len = 0
        def dfs(node, direction, length) -> int:
            nonlocal max_len
            if not node:
                return
            if direction == 'L':
                dfs(node.right, 'R', length + 1)#right: length + 1
                dfs(node.left, 'L', 1)#left: restart, reset length to 1
            else:
                dfs(node.left, 'L', length + 1)
                dfs(node.right, 'R', 1)
            max_len = max(max_len, length)
        dfs(root.left, 'L', 1)
        dfs(root.right, 'R', 1)
        return max_len