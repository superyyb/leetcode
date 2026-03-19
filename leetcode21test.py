#yy思路：比较l1，l2每个元素大小，排进
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(0)
        cur = dummy
#创建一个新的节点ListNode(0)，其val属性被初始化为0，并且next属性被初始化为None
# （因为next 属性由于没有在 __init__ 方法中被赋值，所以它保持了默认值 None。）
#dummy不存储链表实际数据，但是可以作为链表起点。dummy.next指向合并链表后的第一个实际节点
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2 #连接剩余的节点
        return cur.next #返回合并后的链表头节点
sol=Solution()
l1 = list_to_linkedlist([1, 2, 4])
l2 = list_to_linkedlist([1, 3, 4])
merged_list=sol.mergeTwoLists(l1, l2)
print(merged_list)
