from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#用queue FIFO
from collections import deque
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        q = deque([(root, root.val)])
        while q:
            curr_node, curr_sum = q.popleft()
            if not curr_node.left and not curr_node.right:
                if curr_sum == targetSum:
                    return True      # ✅ 找到了，直接 True
                continue # 没找到，继续看队列里的其他路径
            if curr_node.left:
                q.append((curr_node.left, curr_sum + curr_node.left.val))
            if curr_node.right:
                q.append((curr_node.right, curr_sum + curr_node.right.val))
        return False
    '''
    注意 千万不要写成
    if not curr_node.left and not curr_node.right:
        return curr_sum == targetSum这会在第一个不满足条件的情况下直接判错
    '''

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # top down method
        # 节点逻辑：
        # 把自己加到叶子节点
        # 叶子节点逻辑：
        # 判断是否==targetSum
        if not root:  # 判断你一开始就不能对空树做 dfs
            return False
#⚠️主函数是否需要判断 if not root，取决于题目对“空树”的语义返回值，是否等同于 dfs(base case) 的返回值。
        def dfs(root, curr_sum)->bool:
            if not root:  # 到达「空孩子」时的终止条件，帮你在遍历树时安全地停止
                return False
            curr_sum += root.val  # 「当前路径和」必须包含当前节点的值，一定要先加curr_sum再判断叶子节点
            if not root.left and not root.right:
                return curr_sum == targetSum

            return dfs(root.left, curr_sum) or dfs(root.right, curr_sum)

        return dfs(root, 0)
'''
为什么 DFS 可以直接写 return curr_sum == targetSum？
他不怕第一个叶子没找到路径就直接 return False 吗？
那不就提前结束整个递归了吗？

✔ 答案：不会提前结束，也不会错。
✔ 因为这个 return False 只是“当前递归分支”的返回值，不会影响其它分支继续搜索。
✔ 整个递归只有在所有分支都返回 False 时，才会最终得到 False。
 因为return dfs(root.left, curr_sum) or dfs(root.right, curr_sum)
 只有左右都返回 False → 父节点才返回 False


'''



#target - root.val
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        curr_sum = targetSum - root.val
        if not root.left and not root.right:
            return curr_sum == 0
        return self.hasPathSum(root.left, curr_sum) or self.hasPathSum(root.right, curr_sum)

#入stack解法：
class Solution:
    def hasPathSum(self,root:Optional[TreeNode],targetSum: int)->int:
        if root is None:
            return False
        stack=[(root,root.val)]
        while stack:
            cur_node,cur_sum=stack.pop()
            if cur_node.left is None and cur_node.right is None:
                if cur_sum==targetSum:
                    return True
            if cur_node.right:
                stack.append((cur_node.right,cur_node.right.val+cur_sum))
            if cur_node.left:
                stack.append((cur_node.left,cur_node.left.val+cur_sum))
        return False



d = deque([1, 2, 3, 4])
d.append(5)  # d 变为 deque([1, 2, 3, 4, 5])
d.appendleft(0)  # d 变为 deque([0, 1, 2, 3, 4, 5])
right_elem = d.pop()  # 返回 5，d 变为 deque([0, 1, 2, 3, 4])
left_elem = d.popleft()  # 返回 0，d 变为 deque([1, 2, 3, 4])