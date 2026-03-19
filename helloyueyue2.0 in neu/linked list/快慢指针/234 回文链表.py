class Solution:#创建新链表为原链表的反转链表，判断两个链表是否相等
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #invert list与原来list相同，即为True
        dummy = ListNode(0)
        curr = head
        while curr: #dummy->curr
            new_node = ListNode(curr.val) #这里不能直接改变curr，这样就改变了原链表的结构
            new_node.next = dummy.next #curr.next后面接None
            dummy.next = new_node
            curr = curr.next
        p1 = head
        p2 = dummy.next
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True

class Solution:#用list比较
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        return lst == lst[::-1]

#list + two pointers
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        left = 0
        right = len(arr) - 1
        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
        return True
#1 2 3 3 2 1所以“第一个 3”和“第二个 3”一直没有断开
#破坏了后半段的head结构，但前半段和反转后的后半段都能独立遍历，不影响做题判断
class Solution:#取链表中点，将链表后半部分反转，比较前半部分和后半部分是否相等
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tail = slow
        pre = None #pre作为新链表起点
        while tail:
            temp = tail.next
            tail.next = pre
            pre = tail
            tail = temp
        #此时head为完整的原链表，pre为原链表中后段反转，注意不是pre.next
        p1 = head
        p2 = pre
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
    """
    为什么不是pre.next:
    初始： pre = None
    第一轮循环：pre = tail
    最终，pre 会指向反转后链表的头结点，而不是 pre.next。
    你理解的 pre 是 None 那是最开始初始化的值，在 while 循环结束后，pre 已经变成新的头了。
    """

    """
    错误解法：不可以用原地反转把整个链表反过来再比较，会破坏原来的链表结构
    # original = head 只是让 original 指向同一个链表的引用
        reverse = None
        curr = head
        while curr:#原地反转
            temp = curr.next #reverse -> curr -> temp
            curr.next = reverse
            reverse = curr
            curr = temp
        #原链表的方向被完全翻转。head不再连着剩下的节点，它的next 被指向前一个或 None。
        p1, p2 = head, reverse
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
    
    """