# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#recursion
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #单个节点逻辑
        #判断它以及.next是否是相同val
        #如果相同，进入while循环skip所有相同val,return head.next
        #如果不同 直接.next接上递归的后续链表
        if not head or not head.next:
            return head
        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
            return head
        else:
            while head.next and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates(head.next)

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        用双层while循环删掉重复连续值：
        外层while找到重复值x
            内层while删光重复值x的节点
        """
        dummy = ListNode(0, head)
        prev = dummy
        while prev.next and prev.next.next:
            if prev.next.val == prev.next.next.val:#重复
                x = prev.next.val
                while prev.next and prev.next.val == x:
                    prev.next = prev.next.next
            else: #不重复：往前走一格
                prev = prev.next
        return dummy.next