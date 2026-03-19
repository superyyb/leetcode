# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        以dummy为头建立新链表存储答案
        """
        dummy = ListNode(0)
        new_head = dummy
        curr = head.next
        total = 0
        while curr:
            if curr.val != 0:
                total += curr.val
            else:
                new_head.next = ListNode(total)
                new_head = new_head.next
                total = 0 #每次遍历重置total
            curr = curr.next
        return dummy.next #为什么不能return new_head：此时new_head为遍历到最后一位时的节点

#双指针write&curr
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        双指针in-place修改 curr扫描，write写入
        """
        write = head
        curr = head.next
        total = 0
        while curr:
            if curr.val != 0:
                total += curr.val
            else:
                write.next = curr
                curr.val = total
                write = curr #write指针前进
                total = 0
            curr = curr.next
        write.next = None #截断尾巴
        return head.next