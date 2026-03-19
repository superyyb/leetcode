# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy#⚠️curr永远指向需要交换的两节点之前
        while curr.next and curr.next.next:#❌忘记curr.next.next
            temp = curr.next #1
            temp1 = curr.next.next.next #如不提前存 3，链表就断了，找不回来了。
            curr.next = curr.next.next #curr指向2
            curr.next.next = temp #让2指向 1
            temp.next = temp1 #1接后面的链表
            curr = curr.next.next#curr 移动到“下一次要交换的前驱节点”
        return dummy.next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        头插法: 把每一对 (a→b) 看作「子链」[a,b]，
        然后把 b 头插到 a 前面。
        """
        dummy = ListNode(0, head)
        curr = head
        prev = dummy
        while curr and curr.next:
            #反转
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
            #向后移动2步
            prev = curr
            curr = curr.next#此时prev->b->a,因为a，b已经交换，prev直接跳到a，是为两步
        return dummy.next
