# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        crit_idxs = []
        idx = 1
        while curr and curr.next:
            if (curr.val < prev.val and curr.val < curr.next.val) or (curr.val > prev.val and curr.val > curr.next.val):
                crit_idxs.append(idx)
            idx += 1
            prev = curr
            curr = curr.next
        if len(crit_idxs) < 2:
            return [-1, -1] #[3,4,9]
        crit_idxs.sort()
        mini = float("inf")
        for i in range(1, len(crit_idxs)):
            diff = crit_idxs[i] - crit_idxs[i - 1]
            mini = min(mini, diff)
            maxi = crit_idxs[-1] - crit_idxs[0]
        return[mini, maxi]
