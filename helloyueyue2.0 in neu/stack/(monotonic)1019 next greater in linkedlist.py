# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        res = [0] * length
        curr = head
        i = 0
        while i < length:#或者while curr:
            while stack and curr.val > stack[-1][1]:
                index, node = stack.pop()
                res[index] = curr.val
            stack.append((i, curr.val))
            curr = curr.next
            i += 1
        return res
#也可以把链表转为数组再做