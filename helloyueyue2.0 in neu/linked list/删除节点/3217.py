"""
导致超时的原因：没有用set进行nums的查找
"""
#单独判断头节点
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        while head and head.val in nums_set:
            head = head.next #对于头节点不满足要求，直接跳过头节点
        if not head:
            return None
        curr = head
        while curr and curr.next:
            if curr.next.val in nums_set:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
    """
    x in nums 对列表的查找是 O(n) 的,每次检查都要从头到尾扫描一次nums
	而 x in nums_set 对集合的查找平均是 O(1)
    """

#设dummy节点帮助判断
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        nums_set = set(nums)
        while curr.next:
            if curr.next.val in nums_set: #删
                curr.next = curr.next.next
            else:
                curr = curr.next #保留
        return dummy.next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        """
        用prev和curr两个指针遍历链表:
        prev 指向已保留链尾，curr 指向待检查节点
        1 不重复：prev = curr，curr标记为已保留
        2 重复：prev.next = curr.next 当前curr节点被删，prev 续链
        """
        nums_set = set(nums)
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        while curr:
            if curr.val in nums_set:#重复：跳过curr
                prev.next = curr.next
            else:
                prev = curr#不重复：curr标记为已保留
            curr = curr.next#不管跳过还是保留，都需要遍历链表
        return dummy.next


