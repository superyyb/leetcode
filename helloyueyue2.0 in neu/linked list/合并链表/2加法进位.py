# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:#链表都加完后，单独检查 carry 是否还有进位，carry 加成一个新节点
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            if l2:
                val2 = l2.val
            else:
                val2 = 0
            total = val1 + val2 + carry #每次total重新赋值，不用显式重置
            carry = total//10
            curr.next = ListNode(total%10)
            curr = curr.next
            if l1:#移动指针前判断l1,l2是否存在
                l1 = l1.next
            if l2:
                l2 = l2.next
        # if carry: #这句和while l1 or l2 or carry:二选一
        #     curr.next = ListNode(carry)
        return dummy.next

    """
     node = ListNode(1) 创建了一个节点，值是 1，指向 None
     注意 这里的1是value 不是index，链表里没有index概念，只能一个一个数过去
     """

#傻瓜做法 不停str转int转str
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = s2 = ""
        curr = l1
        while curr:
            s1 += str(curr.val)
            curr = curr.next
        curr = l2
        while curr:
            s2 += str(curr.val)
            curr = curr.next
        total = int(s2[::-1]) + int(s1[::-1])
        dummy = ListNode(0)
        curr = dummy
        for t in str(total)[::-1]:
            curr.next = ListNode(int(t))
            curr = curr.next
        return dummy.next