# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: #复杂
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        curr = head
        total = size = index = 0
        while curr:
            size += 1
            curr = curr.next
        curr = head
        while curr:
            total += curr.val*2**(size - 1 - index)
            index += 1
            curr = curr.next
        return total

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decimal = 0
        while head:
            decimal = decimal * 2 + head.val
            head = head.next
        return decimal
    """
    把已经读过的二进制位往左移一位 (×2), 再把当前位加到最低位上
    1*2 + 1
    2 * 2 + 0
    
    """