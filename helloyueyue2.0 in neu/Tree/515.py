# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # main rule: check if is the largest node in a level
        res = []
        if not root:#base case
            return []
        q = deque([root])
        while q:#控制每一层（整体）
            max_val =  float('-inf')
            for i in range(len(q)):#控制当前层的节点
                curr_node = q.popleft()
                max_val = max(max_val, curr_node.val)
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            res.append(max_val)
        return res
