from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
遍历型（Traversal）：没有利用返回值，只是靠外部变量（累加器）更新最大值。
分治型（Divide & Conquer）：每个递归调用都返回一个结果，父调用通过合并子结果得到答案。
"""
# 分治 Bottom-Up 是“子树算完返回深度，父节点再 +1”。
class Solution:
    # 当前节点逻辑
    # 找到并return目前左右子树最高的那个max(left, right)+当前节点高度
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l_depth=self.maxDepth(root.left)
        r_depth=self.maxDepth(root.right)
        return max(l_depth,r_depth)+1
    """
    访问是自上而下，计算和累加是自下而上。
在这段递归里，真正“加 1”并产生返回值的动作，都是在递归“回溯”（unwinding）阶段发生的：
	1.	自上而下遍历（调用阶段）
	•	你从根节点开始，一直往左、往右递归调用 maxDepth，并不在这一阶段做任何加法或返回深度（除了碰到 None 才返回 0）。
	•	这相当于在“探路”：你只是不断钻到树的最底层。
	2.	自下而上回溯（返回阶段）
	•	当某个节点的左右子节点都已经调用并返回深度后，才会执行return max(l_depth, r_depth) + 1
    """

#累加器 自上而下（到空节点时结算）
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_height = 0
        def dfs(root, height):
            nonlocal max_height
            if not root:#在到达空节点时更新height
                max_height = max(max_height, height)
                return
            dfs(root.left, height + 1)
            dfs(root.right, height + 1)
        dfs(root, 0)
        return max_height

# 累加器 自上而下
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node: Optional[TreeNode], depth: int):
            if not node:
                return
            self.ans = max(self.ans, depth) #只要进入节点时就更新max
            # 递归左右子树，深度 +1
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 1)  # depth of root: start from 1
        return self.ans

#分治 Top-Down 是“带着深度往下走，到叶子结算”。
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, height):
            if not root:#当叶子走到底时，传回什么
                return height
            left_h = dfs(root.left, height + 1)
            right_h = dfs(root.right, height + 1)
            return max(left_h, right_h)
        return dfs(root, 0)
"""
    1
   / \
  2   3
  执行：
dfs(1,0)
→ dfs(2,1) → dfs(None,2)(因为root为2不为空，还要继续递归)→ return 2
→ dfs(3,1) → dfs(None,2) → return 2
于是根节点拿到 left_h=2, right_h=2 → return 2
"""


#BFS算法：
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 1)])
        if not root:
            return 0
        while queue:
            node, depth = queue.popleft()
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return depth
"""
为什么BFS不用考虑left right取max depth
BFS 本身就保证了「逐层遍历」；
	•最后访问到的节点一定在最深层；
	•所以 depth 最后一次的值就是最大深度。
"""

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])  # 只存节点
        depth = 0              # 在外面维护深度
        while queue:
            level_size = len(queue)
            for _ in range(level_size):# 处理当前层的所有节点
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1# 当前层处理完，深度加一
        return depth

#stack
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return max_depth
