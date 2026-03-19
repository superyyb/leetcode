class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    """
      每个节点的左子树和右子树本身就是一棵小树。
  所以，我们写的 preorder(root) 这个函数，也可以用来处理 root.left 和 root.right —— 这就是递归的本质：
      “用同一个函数来处理结构相同但规模更小的子问题。”
      你可以把 preorder(root) 想象成一个“会处理一棵树”的工人。这个工人接受一个“树根”，然后做三件事：
      1.	处理自己（把根节点的值加入列表）
      2.	找左子树说：“你来处理你的这棵树”
      3.	找右子树说：“你也来处理你的这棵树”
      """

"""
  外部“累加器”模式（Accumulator： res 定义在 helper 之外，外部收集结果，递归函数只“访问”＋“深入”，不返回有用值。
只是在“告诉”递归函数「去做一件事」，而不是依赖它返回什么值。
当 preorder(None) 被调用时，它马上执行 if node is None: return，
什么都不加到 res，就返回了。既然安全，就不需要额外的空值判断。
	所以在这可以只写return,不用写return []
"""
class Solution(object):#recursion
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        res = []
        def preorder(root):
            if root is None:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)#运行preorder函数
        return res

"""
 “返回值”模式：函数自己返回一个新列表，子问题的结果通过 return 汇合。
1.为什么必须要 return []？
    因为这个函数依赖它的返回值来累积结果。如果你在空节点处不 return []，
    函数就会默认返回 None，接下去做 res += None 就会出错（类型不匹配）。
"""
class Solution(object):#only one function
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        res=[]
        if not root:
            return []
        res.append(root.val)
        if root.left:
            res+=self.preorderTraversal(root.left)
        if root.right:
            res+=self.preorderTraversal(root.right)
        return res

class Solution:#写 if root.left:主要是为了避免对 None 再递归一次
    # 不判断if root.left:也可以，因为当 root.left 是 None，
    # self.preorderTraversal(None) 会一开始就命中 if not root: return []，
    # 直接返回空列表，再拼接就什么都不加了
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        res.append(root.val)
        res += self.preorderTraversal(root.left)
        res += self.preorderTraversal(root.right)
        return res

class Solution(object):#interation
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        # preorder:root,left,right
        # pop stack order: right left root
        # 因为栈是后进先出（LIFO），我们要反着压
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            cur = stack.pop()
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            res.append(cur.val)
        return res

"""
每次先push右再push左，保证了左子树节点会先被pop出来。
右子树的节点虽然早进栈，但会被压在左子树节点下面，直到左子树完全遍历完才出来。
"""


def main():
    sol=Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(sol.preorderTraversal(root))

if __name__=="__main__":
    main()
