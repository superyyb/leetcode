# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            #此时prev是反转后的链表
        dummy = ListNode(0, prev) #dummy.val = 0，dummy.next = prev
        max_val = float("-inf")
        prev = dummy   # prev指向当前节点curr的前驱
        curr = prev #curr指向链表真正第一个元素
        while curr:
            if curr.val >= max_val:
                max_val = curr.val
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next #删除curr
                curr = prev.next #检查下一个节点
        """
        prev 永远是“最后一个被保留的节点”
        curr 永远是“下一个要检查/可能删除的节点”，
        """
        #再次反转
        prev = None
        curr = dummy.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev