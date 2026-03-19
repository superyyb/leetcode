'''
#yy思路：先把链表转为set里的元素，再重新转为链表。
#（但是由于set特征为无序不重复，因此转为链表后要重新排序）
#1.创建一个空 set。
#2.遍历链表，将每个节点的值添加到 set 中
class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None
    head=ListNode(0)
class Solution:
    def DeleteRepetitiveElements(self,l:LinkedList,s:set)-> LinkedList:
#如何将链表转换为set
s=set()
cur=head#先让当前元素从表头开始
while cur:
    s.add(cur.val)#将链表中的值加入到set中
    cur=cur.next #移动到下一个节点
#将set转为链表
dummy=ListNode(0)
now=dummy
for val in s:
    无法保留顺序
    '''


#更简单的思路：将链表中的元素与下一个元素比对，若相同，则当前元素next指针指向下一个元素next指针
class Solution:
    def deleteDuplicates(self,head):#为啥这里写的是head不是x
        now=head #初始化一个指针 now，指向链表的头节点。
        while head:#遍历链表指针，直到指针为None
            while head.next and head.val==head.next.val:
        #首先检查head.next是否存在，再检查是否元素重复
                head.next=head.next.next
        #head.next 获取当前节点的下一个节点，将其 next 属性更新为跳过一个节点
            head=head.next #指针移动到下一个节点
        return now #返回原始节点now

#定义一个链表
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(2)
head.next.next.next=ListNode(3)