# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: #time: O(L) L为链表长度 space:O(1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        前后指针：
        1.令 fast、slow 都指向 dummy；
	    2.fast 先向前走 n+1 步，与slow保持 n 个节点的距离；
	    3.同时移动二者，直到 fast 到达链表末尾（None）；
	    4.此时 slow.next 就是要删的节点
        """
        dummy = ListNode(0, head)#❌(12.18)一定要设置dummy，否则无法删除头节点
        fast = slow = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
    """
如 1-2-3-4-5删去4
结束时 fast 在 None，slow 在 3，刚好 slow 指向被删节点（4）的前一个节点。
     """

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        for i in range(n):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        暴力做法（耗时）：先while loop计算一遍链表长度，
        再for loop删除正数第(length - n)个的节点
        """
        curr = head
        length = 0
        i = 0
        while curr:
            curr = curr.next
            length += 1
        dummy = ListNode(0, head)  # 用 dummy 统一处理删除头结点的情况
        prev = dummy
        # 让prev停在被删节点的前一个位置：index = length - n - 1
        steps = length - n
        for _ in range(steps):
            prev = prev.next
        # 此时 prev.next 就是要删的节点
        prev.next = prev.next.next
        return dummy.next

