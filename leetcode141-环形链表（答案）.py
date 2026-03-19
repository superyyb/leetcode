'''
public class Solution:
    public boolean hasCycle(ListNode head)
        Set<ListNode> seen = new HashSet<ListNode>()
        while (head != null):
            if (!seen.add(head)):
                return true

            head = head.next

        return false;
'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
