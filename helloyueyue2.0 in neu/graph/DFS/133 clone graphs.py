
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    #用hash记录，key为原node value为clone node
        if not node:
            return node
        seen = {}
        def dfs(node):#design dfs to return the copy(as commanded)
            if node in seen:#node has been cloned
                return seen[node]
            copy = Node(node.val)# node has not been cloned
            """
            调用题目定义的 Node 构造函数, Node(node.val) 会新建一个节点：
            •val = 当前节点的值
            •neighbors = 空列表（因为没传，默认 []）
            此时的 copy 就是「只复制了值，但还没连接邻居」的壳子。
            """
            seen[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))  # 递归克隆邻居并加入
            return copy
        return dfs(node)