#naive solution 完全没有用到BST性质
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        queue = [root]
        while queue:
            for i in range(len(queue)):
                curr = queue.pop(0)
                res.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        res.sort()
        return res[k - 1]
"""
BST inorder traversal: left-root-right
就是节点升序排列，用dfs先遍历root.left,再遍历root.right
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        res = []
        def dfs(root):
            if not root:
                return
            nonlocal res
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res[k - 1]

#优化《不用列表存储节点，用外部累加器res 遇到k th节点直接返回
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        def dfs(root):
            nonlocal k
            nonlocal res
            if not root:
                return
            dfs(root.left)
            k -= 1
            if k == 0:
                res = root.val
            dfs(root.right)
        dfs(root)
        return res

#不要外部累加器，层层return出结果
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            nonlocal k
            if not node:
                return None
            left = dfs(node.left)
            if left is not None:#❕这个步骤不能省，只有在左子树找到答案才可以提前return
                return left
            k -= 1
            if k == 0:
                return node.val #核心逻辑
            return dfs(node.right)
        return dfs(root)
