
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #node logic:
        #<p <q: root.right
        #>p >q: root.left
        #else: return root
        if not root:
            return None
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

"""
In a BST:
	•	If both p and q are less than root, LCA is in the left subtree.
	•	If both are greater than root, LCA is in the right subtree.
	•	Otherwise, root is the LCA.
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
    p q都比root大，搜索right
    p q都比root小，搜索left
    在两边 即答案是root
        """
        if not root:
            return None
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:#这样写累赘，最好用上面的 直接else概括
            return root
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
