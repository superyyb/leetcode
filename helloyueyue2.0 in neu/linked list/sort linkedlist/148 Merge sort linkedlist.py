# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Merge Sort:Divide and Conquer
        1.Split: Quick-slow pointer
        2.Sort recursively
        3.Merge
        '''
        if not head or not head.next: #Base case
            return head
        fast = slow = head
        while fast and fast.next:
            pre = slow
            fast = fast.next.next
            slow = slow.next
        mid = slow #The head of right part
        pre.next = None #Split from the end of left part
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    def merge(self, l1, l2) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2 #别漏了
        return dummy.next