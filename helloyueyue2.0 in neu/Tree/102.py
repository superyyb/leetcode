class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: [TreeNode]):
        if not root:
            return []
        queue=[root] #或者queue = deque([root])  cur_node=queue.popleft()
        res=[]
        while queue:
            level=[]
            for i in range(len(queue)):
                cur_node=queue.pop(0)
                level.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            res.append(level)
        return res
"""
遍历每个节点恰好一次，总共 O(n)。
	队列：最多同时存储一层节点，最坏情况（满二叉树底层）可接近 n/2，O(n)。
	•	结果列表 res：存储了所有节点值，也需要 O(n)。
	•	合计：O(n)。
"""

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        def DFS(root:Optional[TreeNode],level:int):
            if not root:
                return []#[[3],[9,20],[15,7]]
            if len(res)==level:#有几层就创建几个[]
                res.append([])
            res[level].append(root.val)#往[]里加入root.val
            DFS(root.left,level+1)
            DFS(root.right,level+1)
        DFS(root,0)
        return res
"""
时间复杂度
	•	递归访问每个节点一次，且每次操作（append、索引、长度判断）都是 O(1)，因此总共 O(n)。
空间复杂度
	•	递归栈深度：最坏情况下（退化成链表）深度为 n，O(n)；最好是平衡树时深度为树高O(log n)。
	•	结果列表 res：同样存储所有节点值，O(n)。
	•	合计：最坏 O(n)，平均（平衡树）O(n) 但栈额外 O(log n)。
"""