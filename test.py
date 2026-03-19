# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self,p1,p2):
        dummy=ListNode() #dummy是虚拟头节点，也是ListNode类的实例
        curr=dummy #curr是指针，指向当前节点（dummy）
        #????都有list了为什么要设一个dummy
        # p1,p2=list1,list2 #p1,p2分别指向list1和list2这两个链表的头部节点

#比较两个list的节点值
        while p1 and p2:
            if p1.val<=p2.val:
                curr.next=p1#????p1不是一个list么，要把整个p1接在list里面，
                # 不应该只是p1里一个元素接进去么
                p1=p1.next
            else:
                curr.next=p2
                p2=p2.next
            curr=curr.next