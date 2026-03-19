# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#dfs解法 先沿着最左边建立起level_sums = []，再对每个节点判断 是否是本层第一个
#是则新建index，不是则加入到旧的里面
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        '''
        dfs:
        logic for single node:
        if it's start of a new level: index + 1
        else: Add its value to the level_sums
        Use a parameter to store the level
        '''
        level_sums = []
        def dfs(root, level):
            if not root:
                return
            if level == len(level_sums):
                level_sums.append(root.val)
            else:
                level_sums[level] += root.val
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        max_sum = max(level_sums)
        return level_sums.index(max_sum) + 1
    '''
    root = [1,7,0,7,-8,null,null]
    round1: dfs(1, 0) level = 0, len() = 0 level_sums.append(1)
    round2: dfs(7, 1) level = 1, len() = 1 level_sums.append(7)
    round3: dfs(7, 2) level = 2, len() = 2 level_sums.append(7)
    round4: dfs(None, 3) return
    round5: dfs(None, 3) return
    round6: dfs(-8, 2) level = 2, len() = 3 level_sums[level] += 7
    round7: dfs(0, 1) level = 1, len() = 3 level_sums[level] += 0
    '''

from collections import deque
#最优bfs解法 time O(n) space O(h) h = 树高，最坏O(n）
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        '''
        Calculate the sum of level
        Store and update the smallest level
        '''
        if not root:
            return 0
        q = deque([root])
        max_sum = float('-inf')
        level = 1
        while q:
            curr_sum = 0
            for i in range(len(q)):
                curr_node = q.popleft()
                curr_sum += curr_node.val
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            if curr_sum > max_sum:
                max_sum = curr_sum
                ans_level = level
            level += 1
        return ans_level


#我的bfs解法（略微累赘）
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        '''
        Calculate the sum of level
        Store and update the smallest level
        '''
        if not root:
            return 0
        q = deque([root])
        level_sums = []
        while q:
            curr_sum = 0
            for i in range(len(q)):
                curr_node = q.popleft()
                curr_sum += curr_node.val
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            level_sums.append(curr_sum)
        max_sum = max(level_sums)
        for i in range(len(level_sums)):
            if level_sums[i] == max_sum:
                return i + 1




