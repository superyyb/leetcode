# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        前后指针：
        1.令 fast、slow 都指向 dummy；
	    2.fast 先向前走 n+1 步，与slow保持 n 个节点的距离；
	    3.同时移动二者，直到 fast 到达链表末尾（None）；
	    4.此时 slow.next 就是要删的节点
        """
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n+1):
            fast = fast.next
        while fast:
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
        dummy = ListNode(0, head)
        curr = dummy
        length = 0
        while curr.next:
            length += 1
            curr = curr.next
        curr = dummy
        for _ in range(length - n):
            curr = curr.next
        curr.next = curr.next.next#此时curr是需要被删的节点
        return dummy.next

