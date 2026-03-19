class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        #以上已经涵盖了两树空或任一树空的情况了
        new_root = TreeNode(root1.val + root2.val)
            #递归构建new_root的左右子树
        new_root.left = self.mergeTrees(root1.left, root2.left)
        new_root.right = self.mergeTrees(root1.right, root2.right)
        return new_root