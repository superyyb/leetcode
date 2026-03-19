#yy思路：yy想从链表反着来，到第几个开始不重复了 ，就确定节点
#由于是单向链表，需要先转为list 再转回来
#2.双指针法？i指针遍历headA，j-headB，
class ListNode:
        def __init__(self,x):
            self.val=x
            self.next=None
class Solution:
    def getIntersectionNode(self,headA:ListNode,headB:ListNode):
        lstA=[]
        lstB=[]
        current = headA
        while headA:
            lstA.append(headA.val)
            headA=headA.next #容易漏了这一句
        while headB:
            lstB.append(headB.val)
            headB = headB.next
        res_lstA=lstA[::-1]
        res_lstB=lstB[::-1]
        i=0
        if res_lstA[i]!=res_lstB[i]:
            return None
        while i<len(res_lstA) and i<len(res_lstB):
        #错误写法：for i,j in len(res_lstA),len(res_lstB):
            if res_lstA[i] == res_lstB[i]:
                i+=1
            else:
                break
        #从链表头部开始遍历，跳过len-i个节点
        for _ in range(len(res_lstA)-i):
            current=current.next
        return current
        # message2=f"Intersected at {str(res_lstA[i-1])}"
        # return message2
        #不可以这么写，答案要求从链表寻找相交节点，而不是简单的返回相交的那个值

# sol=Solution()
# headA=1->2->
# print(sol.getIntersectionNode())

#简单解法：求出链表长度的差值，长链表的指针先想后移动lenA-lenB。
# 然后两个链表一起往后走，若结点相同则第一个相交点。
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        # 统计两链表长度
        tagA = headA
        len_A = 0
        while tagA != None:
    #找到链表里面最后一个对象， 以此来得出链表的长度
            len_A += 1
            tagA = tagA.next
        tagB = headB
        len_B = 0
        while tagB != None:
            len_B += 1
            tagB = tagB.next
        if len_A == len_B:
            # 两链表一起向前走，直到相交为止
            while headA != headB:
                headA = headA.next
                headB = headB.next
            return headA

#将单链表A和单链表B相差的部分去掉，依次对应比较等长的部分即可。
# 在计算两个链表的长度之后，比较两个链表的尾节点是否一样，
# 如果不一样说明没有交叉节点，返回NULL。
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        pa = headA # 2 pointers
        pb = headB

        while pa is not pb:
            # pa先遍历headA，然后再遍历headB
            # pb先遍历headB，然后再遍历headA
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa
        # 只有两种方式结束循环，一种是pa和pb所指相同，另一种是headA和headB都已经遍历完仍然没有找到。