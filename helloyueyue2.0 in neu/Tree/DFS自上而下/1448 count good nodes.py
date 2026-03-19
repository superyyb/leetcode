"""
错误做法❌
在递归中把max_val当作一个全局共享变量修改，会污染兄弟子树的搜索路径
应该每一条路有自己的max_val,把max_val作为参数进入递归
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 0
        max_val = 0
        def dfs(root):
            if not root:
                return
            nonlocal count
            nonlocal max_val
            if root.val >= max_val:
                count += 1
            max_val = max(max_val, root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return count

#累加器
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #当前节点逻辑
        #如果比max_val大，count + 1
        #维护更新max_val
        if not root:
            return 0
        count = 0
        def dfs(root, max_val):
            nonlocal count
            if not root:
                return
            if root.val >= max_val:
                count += 1
                max_val = root.val
            dfs(root.left, max_val)
            dfs(root.right, max_val)
        dfs(root, float('-inf'))
        return count

#函数式
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def countpaths(root, max_val):
            if not root:
                return 0
            if root.val >= max_val:
                count = 1
                max_val = root.val
            else:
                count = 0
            return (count +
            countpaths(root.left, max_val) +
            countpaths(root.right, max_val))
        return countpaths(root, root.val)
    """
   
if root.val >= max_val:
            count = 1  
            max_val = root.val
        else:
            count = 0
 等同于 count = 1 if root.val >= max_val else 0,  max_val = max(root.val, max_val) #这样写更保险
    """

