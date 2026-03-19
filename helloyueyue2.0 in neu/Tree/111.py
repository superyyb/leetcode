from typing import Optional,List
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
       #累加器
        min_depth = float("inf")
        if not root:
            return 0
        def dfs(root, depth):
            if not root:
                return
            nonlocal min_depth
            if not root.left and not root.right:#在叶子节点处更新
                min_depth = min(min_depth, depth)
                return
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 1)
        return min_depth

#bottom-up
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 当前节点逻辑：
        # 如果只有左子树：return right + 1
        # 如果只有右子树：return left + 1
        # 找到并return目前最小的depth=min(left, right) + 1
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not root.left:#没有左子树
            return right + 1
        if not root.right:#没有右子树
            return left + 1
        return min(left, right) + 1
"""
111 min_depth和104 max_depth用分治的区别：
104:
空节点：返回 0，因为空子树不贡献高度。
非空节点：父节点深度 = max(左子树深度, 右子树深度) + 1。
max 不会因为 0 被误选，因为即使某边是空，另一边的深度更大。所以 0 合理。

111:
空节点：返回 0。
•关键区别：
	如果直接 min(left, right) + 1，空子树 0 会被选中，导致错误。必须排除空子树：
	•单边树时，只能走非空子树。
	•双边树时，才取 min(left, right)。
"""

class Solution:#分治 up down
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(root, depth):
            if not root:
                return
            if not root.left and not root.right:
                return depth
            left_d = dfs(root.left, depth + 1)
            right_d = dfs(root.right, depth + 1)
            if not root.right:
                return left_d
            if not root.left:
                return right_d
            return min(left_d, right_d)
        return dfs(root, 1)

from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
      #BFS 只要遇到左右孩子都为空时 说明遍历到最低点了 直接返回depth
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            # 第一次遇到叶子就是最小深度
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))






