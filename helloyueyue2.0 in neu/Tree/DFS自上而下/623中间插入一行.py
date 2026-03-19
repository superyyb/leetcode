class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        def dfs(root, curr_depth):
            if not root:
                return
            if curr_depth == depth - 1:
                left = TreeNode(val)
                right = TreeNode(val)#像链表一样，新节点头尾分别衔接好原二叉树节点
                left.left = root.left
                right.right = root.right
                root.left = left
                root.right = right
            else:
                dfs(root.left, curr_depth + 1)
                dfs(root.right, curr_depth + 1)
        dfs(root, 1)
        return root