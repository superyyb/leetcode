#从 dummy 开始”是为了找到那个“值刚好大于 curr 的节点”的“前一个节点”。
#在singly linkedlist中，这是Re-link pointers的唯一办法。

# time: worst O(n2) space: O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1.Maintain a sorted part at the beginning of the list
        2.Repeatedly compared the first unsorted element with the tail of sorted part
        3.If it's smaller, insert it into its correct position by traversing from the head; otherwise, simply extend the sorted portion.
        '''

        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        lastSorted = head
        curr = head.next
        while curr:
            if curr.val >= lastSorted.val:  # Curr node is already in right position
                lastSorted = lastSorted.next
            else:  # 1 -> 3 -> 4 -> 2
                pre = dummy
                while pre.next.val <= curr.val:
                    pre = pre.next
                # pre:1 curr:2 lastSorted:4
                lastSorted.next = curr.next  # 4 -> None
                curr.next = pre.next  # 2 -> 3
                pre.next = curr  # 1 -> 2
            curr = lastSorted.next  # ❌curr = curr.next
        return dummy.next



