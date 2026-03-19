class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:#注意target是original上的
        if not original:
            return None
        if original == target:
            return cloned
        return (self.getTargetCopy(original.left, cloned.left, target)
                or self.getTargetCopy(original.right, cloned.right, target))
        #关心结果，为了拿到 cloneTree(root.left)的返回值来赋值给新的 left，所以需要加return