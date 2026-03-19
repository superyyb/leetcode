# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next  # 1) 先拿到后半段表头
        slow.next = None  # 2) 再把前后两段断开 ⚠️1,2顺序不能乱
        pre = None  # pre cur temp
        cur = second
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        second = pre  # 反转之后pre是新head
        # 开始交错reorder
        first, second = head, pre
        while first and second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        """
        first,  temp1
        second, temp2
        """


"""
merge two lists:
其实就是把链表接好以后，把 first、second 往后挪，准备处理下一轮。
永远是first -> second
"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head  # [1,2,3,4,5,6,7]
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
