#累加器
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        #how to keep the parent and grandparent
        #send them as parameters
        #节点逻辑：
        #判断它的grandparent是否为偶数
        total = 0
        def dfs(node, parent = None, grandparent = None):
            nonlocal total
            if not node:
                return
            if grandparent and grandparent.val % 2 == 0: #避免grandparent是NoneType报错
                total += node.val
            dfs(node.left, node, parent)
            dfs(node.right, node, parent)
        dfs(root, None, None)
        return total
    """
    不用定义if root.left or root.right:
                parent = root
    因为dfs(node.left, node, parent)已经表明：
    •	下一层的 node 是当前的 node.left
	•	下一层的 parent 是当前的 node
	•	下一层的 grandparent 是当前的 parent
    """

#函数式
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent = None, grandparent = None):
            if not node:
                return 0
            val = node.val if grandparent and grandparent.val % 2 == 0 else 0
            return val + dfs(node.left, node, parent) + dfs(node.right, node, parent)
        return dfs(root, None, None)