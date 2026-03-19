#典型自底向上DFS，返回每一层的值给父节点
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right: #叶子节点
            return False if root.val == 0 else True
        left = self.evaluateTree(root.left) #分别左右递归
        right =  self.evaluateTree(root.right)
        if root.val == 2:  #or       #合并子树返回值返回到父节点
            return left or right
        else:
            return left and right