class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def is_symmetric(tree: TreeNode) -> bool:
    if tree is None:
        return True
    def recursion(left,right)->bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return left.data==right.data and recursion(left.left,right.right) and recursion(left.right, right.left)
    return recursion(tree.left,tree.right)

def main():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(2)
    tree.left.left=TreeNode(3)
    tree.left.right = TreeNode(4)
    tree.right.left = TreeNode(4)
    tree.right.right = TreeNode(3)
    print(is_symmetric(tree))

if __name__ == "__main__":
    main()
