# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#显式计算链表长度
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #只需swap values，双指针分别定位到两个k th，交换值
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        if k == 0 or not head:
            return head
        dummy = ListNode(0, head)
        front = end = dummy
        for _ in range(k):
            front = front.next
        for _ in range(length - k + 1):
            end = end.next
        front.val, end.val = end.val, front.val
        return head

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(k):
            fast = fast.next
        front = fast #存储fast节点作为第一个k th节点
        while fast:
            fast = fast.next
            slow = slow.next
        end = slow
        front.val, end.val = end.val, front.val
        return head
    """
    初始化dummy，则while fast:
    直接将fast = head，则while fast.next
    """

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        fast = slow = head
        for _ in range(k - 1):
            fast = fast.next
        front = fast #存储fast节点作为第一个k th节点
        while fast.next:
            fast = fast.next
            slow = slow.next
        end = slow
        front.val, end.val = end.val, front.val
        return head