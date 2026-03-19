# 新增一个变量 odd，用于判断当前层数是奇数层，还是偶数层。
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:#如果是空树
            return []
        queue=[root]
        res=[]
        odd=True # odd 为 True 表示奇数层（从左到右），False 表示偶数层（从右到左）
        while queue:
            level = []
            for i in range(len(queue)):
                current_node = queue.pop(0)
                if odd:
                    level.append(current_node.val)
                else:
                    level.insert(0, current_node.val)
                    # insert(0, element) ，在索引 0 的位置插入element，也就是插入到列表的最前面
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            res.append(level)
            odd=not odd
        return res

#或者利用level[::-1]
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        flag = True
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if flag:
                res.append(level)
            else:
                res.append(level[::-1])
            flag = not flag
        return res