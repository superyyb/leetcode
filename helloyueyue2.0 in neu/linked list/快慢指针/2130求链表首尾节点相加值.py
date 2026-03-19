# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_val = float("-inf")
        """
        把原链表后半段反转为p2，p1，p2节点值分别相加，比较出max_val
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tail = slow
        pre = None
        while tail:
            temp = tail.next
            tail.next = pre
            pre = tail
            tail = temp
        p1 = head
        p2 = pre
        while p1 and p2:
            val = p1.val + p2.val
            max_val = max(max_val, val)
            p1 = p1.next
            p2 = p2.next
        return max_val