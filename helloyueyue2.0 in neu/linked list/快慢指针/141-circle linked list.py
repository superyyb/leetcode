class Solution:#集合法
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited=set()
        curr = head
        while curr:
            if curr not in visited:
                visited.add(curr)
            else:
                return True
            curr = curr.next
        return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited=set()
        curr = head
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next
        return False

class Solution:#快慢指针
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
    """
为什么不用写成while fast.next and fast.next.next:
    1. 条件 while fast and fast.next 意味着：fast 不是 None并且 fast.next 也不是 None
    2. 在循环体中，执行 fast = fast.next.next这一步会访问 fast.next.next，是否安全？
    是的，因为你在进入循环前就确保：
    •	fast 本身存在；
    •	fast.next 存在；
    所以 fast.next.next 要么是个节点，要么是 None，但它至少是“合法访问”的，不会导致异常。
    """