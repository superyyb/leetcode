# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        """
        第a-1个节点 之前 保留list1
        第a到b个节点 拼接到list2
        list1[0..a-1] → list2 → list1[b+1..end]
        """
        dummy =  ListNode(0, list1)
        prevA = dummy
        for _ in range(a):
            prevA = prevA.next
        endB = prevA #list1第b个节点：endB
        for _ in range(b - a + 1):
            endB = endB.next
        postB = endB.next #list1第b+1个节点：postB
        prevA.next = list2 #把list2接入endB
        tail = list2 # 找到 list2 尾节点 tail
        while tail.next:
            tail = tail.next#用while找到list2的尾部
        tail.next = postB #把list2尾部接回list1后半段
        return dummy.next