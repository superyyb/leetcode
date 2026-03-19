# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        curr永远指向res list里的最后一个node，方便把后面的节点接上去
        为什么一定要加入list_index:heap必须比较出大小，如果两个node.val一样，python不能比较node
        '''
        #time: O(Nlogk) space:O(k)
        heap = []
        for list_index, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, list_index, node))
        dummy = ListNode()
        curr = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next