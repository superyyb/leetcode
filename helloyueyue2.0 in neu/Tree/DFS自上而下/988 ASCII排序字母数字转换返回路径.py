# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        #python中字符串可以按ASCII比较大小
        def dfs(root, path):
            if not root:
                return "~"  # "~" > 'z'，保证它永远比正常路径大，避免出现none和正常路径比较的报错

            char = chr(ord('a') + root.val) #数字转换为对应字母的常见方法
            path = char + path
            if not root.left and not root.right:
                return path
            return min(dfs(root.left, path), dfs(root.right, path))
        return dfs(root, "")

    """
    chr(ord('a') + 0)  →  chr(97)  →  'a'
    chr(ord('a') + 1)  →  chr(98)  →  'b'
    chr(ord('a') + 25) →  chr(122) →  'z'
    """
