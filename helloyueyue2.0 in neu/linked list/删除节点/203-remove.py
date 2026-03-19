# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #可以删除，后面while head已经判断了head是否为空
        # if not head:
        #     return head
        #如果头节点是val：
        while head and head.val == val:
            head = head.next
        curr = head#curr从head开始，这样如果curr.next值=val时，可以记录到它的上一个节点
        while curr and curr.next:#curr和curr.next都不能为空
            if curr.next.val == val:
                curr.next = curr.next.next#删除
            else:
                curr = curr.next#遍历接着找
        return head

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head#定义一个dummy，让他指针指向head
        curr = dummy
        while curr.next:#如果curr.next不为空时，dummy.next 永远不会变，只有 curr 在变，用curr遍历链表
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next#dummy.next才是我们定义的新链表的head

#用dummy新建链表
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        curr = head
        while curr:
            if curr.val != val:
                tail.next = curr
                tail = curr
            curr = curr.next
        tail.next = None #最后要断开尾部，否则可能形成环
        return dummy.next