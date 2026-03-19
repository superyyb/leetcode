# yy思路：pos为-1，无环形，返回False；pos为index，返回True
# 如何判断环形：从head开始遍历链表中元素，比较当前元素是否之前出现过？
#区别于83题，83题已排序，所以是删除连续重复元素，只要把当前和下一个进行比较即可
#把遍历过的元素放在set中，每遍历当前元素与set中的比较是否重复
#if cur.val in set:
#那万一链表中有重复的元素值怎么办啊
#官方答案用哈希表来存储所有已经访问过的节点，和集合有何不同？
class Solution:
    def CheckDuplicatesElements(self,head):
        s=set()
        cur=head
        if cur.next is None:#列表只有一个元素的情况
            return False
        while cur:
            while cur.val not in s:#区别cur和cur.val，只有cur.val才能列入set
        #只有在s内没有元素（即首次循环时）进入循环
                s.add(cur.val)
                cur=cur.next #指针移动
                if cur.val in s:
                    return True
                else:
                    return False
    '''本来想用
        while cur.next and cur.val not in s:
            xx
        else:
            return False
        发现else的条件是没有cur.next或者cur.val在s 和预想不符
    5，2，3，0，4
    '''

#正确答案：可以用set，但是要存储节点到set里
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set() #定义一个set存储节点
        while head: #遍历节点
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

#快慢指针法：
#创建一个快指针，一个慢指针。快指针一次走两布，慢指针一次走一步。
# 慢指针走一圈，快指针走两圈，如果两个指针指向位置相同了，说明列表是环状的。
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False