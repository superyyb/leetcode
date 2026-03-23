# Mar 22 复盘
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(p, q):
            '''
            dfs(p, q) 回答的问题是：p 和 q 这两棵子树，是不是镜像？
            Logic:
            Compare two subtrees(p, q)
            '''
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return dfs(p.left, q.right) and dfs(p.right, q.left)
        return dfs(root.left, root.right)



#比较时要先把节点为空的情况弄清楚，要不然就是操作空节点
# 并且镜像：左子树的左节点对应右子树的右节点，左子树的右节点对应右子树的左节点
from typing import Optional
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #节点逻辑
        #左右对称位置节点是否相同
        #1.都🈚️ 2.一个🈚️ 3.都🈶比较值 4.递归比较
        if not root:
            return True
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.left, q.right) and isSameTree(p.right, q.left) #关键区别isSameTree：左右“交叉”比较
        return isSameTree(root.left, root.right)

import collections
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None
        queue = collections.deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            left_node = queue.popleft()
            right_node = queue.popleft()
            if not left_node and not right_node:#同样先判断是否空节点
                continue
            if not left_node or not right_node:
                return False
            if left_node.val != right_node.val:
                return False
            queue.append(left_node.left)
            queue.append(right_node.right)
            queue.append(right_node.left)
            queue.append(left_node.right)
        return True
