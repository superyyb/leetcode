Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if not list1:
        #     return list2
        # if not list2:
        #     return list1
        dummy = ListNode(0)
        curr = dummy#不可以写curr = dummy.next这样curr就直接是None了
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next #❕❕❕不管接的是list1还是list2，记得继续往下走curr，别漏了
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        return dummy.next
    """
不用写basecase 因为在 while list1 and list2: 的循环里，
如果一开始其中一个链表就是空的，循环根本不会进入，直接执行while循环后的步骤
    """

class Solution:#recursion
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:#l1比较小，当前节点接l1，l1.next由递归决定
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1 #返回当前这一层决定的链表头
        else:#l2比较小，当前节点接l2，l2.next由递归决定
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
