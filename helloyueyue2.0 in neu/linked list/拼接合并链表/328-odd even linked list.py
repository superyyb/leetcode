# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head


'''
结论：最后一次循环是在哪？

对于2 -> 1 -> 3 -> 5 -> 2 -> 4：最后一次进入循环体是在 even 指向节点 5 的时候。
在这一轮循环中，even 跨越到了最后一个节点 4。
循环结束时，even 停在节点 4，而 odd 停在它前面的节点 2。

为什么这个条件能完美覆盖奇偶两种情况？
长度为偶数时（如此例）： 循环停止是因为 even.next 变成了 None。此时 odd 刚好是奇数部分的最后一个，even 是整个链表的最后一个。
长度为奇数时（如 1-2-3-4-5）： 循环停止是因为 even 本身变成了 None。此时 odd 停在最后一个节点（奇数位），even 已经跳出了边界。
'''