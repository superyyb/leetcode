#yy思路：转为list 双指针？i，j一前一后遍历？
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        if len(lst)<=1:
            return True
        i,j=0,len(lst)-1
        # while i<j:
        #     if lst[i]==lst[j]:
        #         i+=1
        #         j-=1
        #     return True
        # return False

        # while i < j:
        #     if lst[i] == lst[j]:
        #         i += 1
        #         j -= 1
        #     else:
        #         return False
        #     return True

        while i < j:
            if lst[i] != lst[j]:
                return False
            i += 1
            j -= 1
        return True

#根本不用这么复杂：
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        return lst==lst[::-1]

#用递归答题：
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        self.front_pointer = head

        def recursively_check(current_node=head):
        #递归函数，接收一个参数 current_node，默认值为 head
            if current_node is not None:#如果当前节点存在
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()
