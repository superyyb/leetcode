from collections import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#recursion time:O(n) space:O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        假设后面所有的都reverse成功了，你现在只需要处理第一个节点如何reverse
        '''
        #单个节点(head)逻辑：
        #断开和head.next的链接，将head.next.next的连接连到自己
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #用一个 dummy 节点作为“新链表”的头，
    #把原链表中的每个节点拿出来，插到 dummy 后面
        """
        dummy -> None
        curr = 1 -> 2 -> 3 -> 4 -> 5 -> None
        """
        dummy = ListNode(0)#⚠️dummy其实是固定的哨兵节点，固定的入口，永远不要改它，只是它的 .next不断被更新。
        curr = head #初始化，区别于203，直接创建了以dummy为head的新链表，而不是像203那样把dummy加在原链表的头位
        while curr:#dummy curr temp 1<-2<-3<-4
            next_temp = curr.next #暂存curr的下一个节点
            curr.next = dummy.next #1.next = None
            dummy.next = curr #dummy->1->None
            curr = next_temp #把暂存的下一个节点变成curr继续循环
        return dummy.next

class Solution:#原地反转：直接将链表尾巴指向 None，作为起点
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #1->2->3
        pre = None #初始化
        curr = head #1
        while curr:
            temp = curr.next #暂存下一节点
            curr.next =pre #指针反转
            pre = curr #pre=1 更新pre
            curr = temp #curr=2 更新curr
        return pre


