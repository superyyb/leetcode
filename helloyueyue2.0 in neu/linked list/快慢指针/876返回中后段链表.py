class Solution:#快慢指针
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1.idx: length//2+1
        2.快慢指针 fast2步，slow1步
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

class Solution: #两遍遍历笨猪解法
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:## 第一遍遍历：计算链表长度
            curr = curr.next
            length += 1
        curr = head
        for _ in range(length//2): ## 第二遍遍历：移动到中间位置
            curr = curr.next
        return curr