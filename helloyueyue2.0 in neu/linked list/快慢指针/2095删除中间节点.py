class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: #⚠️要排除head只有一个节点的情况！！
            return None
        fast = slow = head
        pre = None #可以先在最前面把pre定义为None，先提出这个节点
        while fast and fast.next:
            fast = fast.next.next
            pre = slow #pre为被删节点的前驱节点
            slow = slow.next
        temp = slow.next
        slow.next = None
        pre.next = temp
        return head