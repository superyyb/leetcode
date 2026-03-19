class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        # root在 inorder左边的所有元素，都是左子树的中序遍历；右边的则是右子树的中序遍历
        separator_idx = inorder.index(root_val)
        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx + 1:]
        # 中序数组大小一定跟前序数组大小是相同的
        preorder_left = preorder[1:1 + len(inorder_left)]
        preorder_right = preorder[1 + len(inorder_left):]
        # recursion
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root
"""
必须要两种遍历才能确定一个树：
1.	preorder 给“根”
	•	preorder 的第一个数是当前子树的根。
	•	但是它自己并不知道“左子树有多少个节点，右子树有多少个节点”。
2.	inorder 给“分界”
	•	在 inorder 里找到根的位置，就能把左子树和右子树分出来。
	•	左边部分 → 左子树的 inorder
	•	右边部分 → 右子树的 inorder
3.	二者结合才能对齐
	•	inorder_left 的长度 = 左子树的节点数。
	•	用这个长度去切 preorder，就能得到对应的 preorder_left。
	•	于是 (preorder_left, inorder_left) 就完全描述了 左子树。
"""