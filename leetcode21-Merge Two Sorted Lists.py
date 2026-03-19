'''
没学链表之前自己的解法：
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1=[]
        list2=[]
        merged_list=list1+list2
        sorted_merged_list=sorted(merged_list)
        return merged_list
sol=Solution()
list_1=[1,2,4]
list_2=[1,3,4]
merged_list=list_1+list_2
print(sol.mergeTwoLists(merged_list))
'''

# Definition for singly-linked list. 单向链表
# class ListNode: 定义一个节点
#     def __init__(self, val=0, next=None):
#         self.val = val 定义元素
#         self.next = next 定义指针
class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy=ListNode() #dummy是虚拟头节点，也是ListNode类的实例
        curr=dummy #curr是指针，指向当前节点（dummy）
        p1,p2=list1,list2 #p1,p2分别指向list1和list2这两个链表的头部节点

#比较两个list的节点值
        while p1 and p2:
            if p1.val<=p2.val:
                curr.next=p1#????p1不是一个list么，要把整个p1接在list里面，
                # 不应该只是p1里一个元素接进去么
                p1=p1.next
            else:
                curr.next=p2
                p2=p2.next
            curr=curr.next


# 测试数据
list1 = [1, 2, 4]
list2 = [1, 3, 4]

# 调用函数进行合并
merged_list = mergeTwoLists(list1, list2)

# 输出合并后的链表
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
print("None")