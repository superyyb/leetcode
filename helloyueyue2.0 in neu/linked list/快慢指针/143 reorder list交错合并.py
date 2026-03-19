# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head  #快慢指针找list中点 [1,2,3,4,5,6,7]
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        pre = None
        while slow:  # [5,6,7]
            temp = slow.next
            slow.next = pre
            pre = slow
            slow = temp
        first, second = head, pre
        while first and second:
            temp1, temp2 = first.next, second.next
            if temp1 is None:  # ❕
                break
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        if first:  # ❕
            first.next = None
