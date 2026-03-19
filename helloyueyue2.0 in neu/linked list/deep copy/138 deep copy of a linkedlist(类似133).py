"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None#不要写return head 语义不清
        seen = {}
        curr = head
        while curr:#1.copy node val
            seen[curr] = Node(curr.val)
            curr = curr.next
        curr = head #遍历第二遍
        while curr: #2.copy pointers新指针指向新节点
            if curr.next:
                seen[curr].next = seen[curr.next]
            if curr.random:
                seen[curr].random = seen[curr.random]
            curr = curr.next
        return seen[head]