#累加器
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # root-leaf
        # 每个节点逻辑：加到path里
        # 叶子节点逻辑：判断path里的节点是否freq都是偶数，最多有一个奇数，则加入到count
        #不需要记录path，直接用字典记录freq
        seen = {}
        count = 0
        def dfs(node):
            nonlocal count
            if not node:
                return
            seen[node.val] = seen.get(node.val, 0) + 1
            if not node.left and not node.right:
                odd = 0
                for v in seen.values():
                    if v % 2 == 1:
                        odd += 1
                if odd <= 1:
                    count += 1
            else:
                dfs(node.left)
                dfs(node.right)
            #回溯：离开节点前把它自己的计数撤销
            seen[node.val] -= 1
            if seen[node.val] == 0:
                del seen[node.val]
        dfs(root)
        return count
'''
比下面的解法快在哪
每进入一个节点：seen[val] += 1
每离开一个节点：seen[val] -= 1

 下面的解法： 每一条路径就算一次counter
'''

class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        # root-leaf
        # 每个节点逻辑：加到path里
        # 叶子节点逻辑：判断path里的节点是否freq都是偶数，最多有一个奇数，则加入到count
        count = 0

        def dfs(root, path):
            nonlocal count
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right:
                c = Counter(path)
                odd = 0
                for freq in c.values():
                    if freq % 2 != 0:
                        odd += 1
                if odd <= 1:
                    count += 1
            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()

        dfs(root, [])
        return count

    """
      回溯一定要在所有分支之后（函数尾部）执行，这样“如果是叶子提前 return”
    和“非叶子正常走完”两种情况都能触及到它。
	  如果把回溯写进了某个分支（比如只写在叶子里），那么其他分支就
	永远不会执行到那段代码，导致状态无法正确复原。
    """