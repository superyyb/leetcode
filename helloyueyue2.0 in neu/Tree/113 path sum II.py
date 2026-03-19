# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#关键❌：在pop前return
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        path = []
        def dfs(node, curr_sum):
            path.append(node.val)
            if not node.left and not node.right:
                if curr_sum == targetSum:
                    res.append(path[:])
                    return
            if node.left:
                dfs(node.left, curr_sum + node.left.val)
            if node.right:
                dfs(node.right, curr_sum + node.right.val)
            path.pop()
        dfs(root, root.val)
        return res

#最优解 time:O(n) space:O(h)
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        path = []
        def dfs(node, curr_sum):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right:
                if curr_sum == targetSum:
                    res.append(path[:])
            if node.left:
                dfs(node.left, curr_sum + node.left.val)
            if node.right:
                dfs(node.right, curr_sum + node.right.val)
            path.pop()
        dfs(root, root.val)
        return res

#backtrack 隐式（）❌时间复杂度太高 最坏O(n2) path + [x] 会新建一个 新列表，拷贝当前 path 里的所有元素
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return res
        def dfs(root, path):
            if not root:
                return
            if not root.left and not root.right:
                if sum(path) == targetSum:#sum(path) 每次都重新算，会变 O(N²)
                    res.append(path)
                    return #记得直接return，叶子没有子节点再下探了，这里写return的话就不适合pop
                #一定要pop的话 在这里的return前再加一句path.pop()
            if root.left:
                dfs(root.left, path + [root.left.val])
            if root.right:
                dfs(root.right, path + [root.right.val])
        dfs(root, [root.val])
        return res

