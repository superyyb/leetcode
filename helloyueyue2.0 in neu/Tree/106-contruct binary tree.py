# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#postorder:left-right-root
#inorder: left-root-right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)
        seperator_idx = inorder.index(root_val)
        inorder_left = inorder[:seperator_idx]
        inorder_right = inorder[seperator_idx+1:]
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):-1]#记得删掉postorder最后那个root
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)
        return root
        #注意slice [:] 左闭右开