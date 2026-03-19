#recursion
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #单个节点逻辑
        #如果和head.next val不重复，直接接上head.next return head
        #如果重复， while skip重复的值，再接上head.next return head
        if not head or not head.next:
            return head
        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
            return head
        else:
            while head.next and head.val == head.next.val:
                head = head.next
            head.next = self.deleteDuplicates(head.next)
            return head

#set记录重复节点（对于sorted array而言大材小用）
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        dummy = ListNode(0, head)
        curr = dummy
        while curr.next:
            if curr.next.val not in seen: #保留
                seen.add(curr.next.val)
                curr = curr.next
            else: #删
                curr.next = curr.next.next
        return dummy.next

#对于有序链表 只需要比较相邻两个节点值是否相同就可
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:#删除时把所有连续重复都清理干净
                curr.next = curr.next.next
            else: ## 不重复，往前走一步
                curr = curr.next
        return head