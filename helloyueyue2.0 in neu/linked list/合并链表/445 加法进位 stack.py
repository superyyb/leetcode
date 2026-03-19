# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:#头插法
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #和lc2不一样，从尾部开始计算，考虑把链表反转
        def reverse(head):
            pre = None
            while head:
                temp = head.next
                head.next = pre
                pre = head
                head = temp
            return pre
        l1 = reverse(l1)
        l2 = reverse(l2)
        carry = 0
        head = None
        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            if l2:
                val2 = l2.val
            else:
                val2 = 0
            total = val1 + val2 + carry
            carry = total // 10
            node = ListNode(total % 10)
            node.next = head  # 头插法关键：新节点指向旧head
            head = node       # 然后更新head为新节点
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head


class Solution: #一直反转链表
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #和lc2不一样，从尾部开始计算，考虑把链表反转
        def reverse(head):
            pre = None
            while head:
                temp = head.next
                head.next = pre
                pre = head
                head = temp
            return pre
        l1 = reverse(l1)
        l2 = reverse(l2)
        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            if l2:
                val2 = l2.val
            else:
                val2 = 0
            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return reverse(dummy.next)

#stack.pop模拟从尾部开始加
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        # Step 1: 把两个链表的值压入栈中
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        carry = 0
        head = None  # 最终链表的头
        # Step 2: 从栈中弹出进行加法（从尾部往前加）
        while s1 or s2 or carry:
            val1 = s1.pop() if s1 else 0
            val2 = s2.pop() if s2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            node = ListNode(total % 10)
            node.next = head  # 头插法
            head = node
        return head