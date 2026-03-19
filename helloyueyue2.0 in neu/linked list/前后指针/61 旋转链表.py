# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, size=0):
        self.val = val
        self.next = next
        self.size = size

#Rotate k % len(linkedlist) times
class Solution:#快慢指针
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:#❌not head防止length为0
            return head
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        k %= length
        if k == 0:#❌防止k为0
            return head
        fast = slow = head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        new_head = slow.next #new_head为新链表中最前面的节点
        slow.next = None
        fast.next = head
        return new_head

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        k %= length
        if k == 0:
            return head#❌Jan7:为什么还要判断一次，因为5 % 5 = 0
        fast = slow = head
        for i in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next#slow points to the previous node of new head
        # 断链 + 重连
        new_head = slow.next#把slow.next命名为新的表头
        slow.next = None#让 slow（也就是节点 3）不再指向 4，断开原链表
        fast.next = head#也就是最后一个节点5重新指向原链表的头1
        return new_head

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        curr = head
        length = 1
        while curr and curr.next:
            curr = curr.next
            length += 1
        tail = curr
        n = k % length
        if n == 0:
            return head
        new_tail = head
        for _ in range(length - n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        return new_head

