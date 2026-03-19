# yy思路：链表转为list，list反转，转为链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode):
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        rev_lst=lst[::-1]
        #r_head=ListNode()
        dummy=ListNode(0)
        cur=dummy
        for val in rev_lst:
            new_node=ListNode(val)#对每个元素val，创建一个新节点new_node
            cur.next=new_node#将new_node 链接到当前节点 cur 的 next 指针上。
            cur=cur.next #移动指针到新节点
        return dummy.next#返回头节点即返回整个链表，因为整个链表被隐式的连接在了一起
        #为什么这里不可以return r_head 因为链表连接在一起，返回第一个节点即可以返回整个链表
    #这里也不可以return cur.next 因为cur的值不断更新，最后指向了none
