# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Mar 5复盘
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        'Path doesn't need to pass through the root'
        (Root.val is small)

        Logic for each node:
        1.Add the value from left and right children and compare with the max val
        2.Return node.val + max(node.left.val, node.right.val)
        '''
        max_sum = float('-inf')
        def dfs(node):
            #base case: node -> null: return 0
            #Return: node.val + max(node.left.val, node.right.val)
            #因为父节点需要知道**子树最多能贡献多少*
            # 负数贡献直接丢弃
            #相信递归结果   → 直接用 dfs(node.left)
            nonlocal max_sum
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            max_sum = max(max_sum, node.val + left + right)
            return node.val + max(left, right)
        dfs(root)
        return max_sum
    '''
    if not node: return 0加了这句之后，就不用判断if node.left: if node.right:了
    
    if not node: return 0 是在递归入口就拦截了 None，所以当你调用 dfs(node.left) 时，
    不管 node.left 是不是 None，都会被这一行安全接住，返回 0
    '''

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #当前节点逻辑：
        #计算当前path sum = curr.val + left + right并更新到max_sum
        #return给上一级max(left, right) + curr.val
        max_sum = float('-inf')
        def dfs(root):
            nonlocal max_sum
            if not root:
                return 0
            left_sum = max(dfs(root.left), 0)#⚠️负数路径必须丢弃
            right_sum = max(dfs(root.right), 0)
            #如果一个子树返回负数，你不能把它加进路径里，拖累整个结果
            max_sum = max(max_sum, left_sum + right_sum + root.val)
            return max(left_sum, right_sum) + root.val
        dfs(root)
        return max_sum

#❌解
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #节点逻辑
        #如果节点小于0 不要加入pathsum ❌就算是负数节点也有可能zuchengdaan
        #真正需要去除的是为负数的left_sum/right_sum
        #每次都更新max_sum
        max_sum = float('-inf')
        if not root:
            return 0
        def dfs(root, curr_sum):
            nonlocal max_sum
            if not root:
                return 0
            if root.val >= 0:
                curr_sum += root.val
            max_sum = max(max_sum, curr_sum)
            left_sum = dfs(root.left, curr_sum)
            right_sum = dfs(root.right, curr_sum)
            return max(left_sum, right_sum) + root.val
        dfs(root, 0)
        return max_sum