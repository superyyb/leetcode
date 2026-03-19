class Solution:#把节点存储到数组里，双指针排序
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        """
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)  # nodes = [Node(1), Node(2), Node(3), Node(4)]
            curr = curr.next
        i, j = 0, len(nodes) - 1
        while i < j:  # [1,2,3,4,5]
            nodes[i].next = nodes[j]
            i += 1
            if i == j:
                break  # 避免继续让j连到i 形成自环
            nodes[j].next = nodes[i]
            j -= 1
        nodes[i].next = None  # 手动设置尾节点的 .next = None。

class Solution:#快慢指针找中点->反转后半链表->merge two linked lists
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head #[1,2,3,4,5,6,7]# 1. 找中点
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        pre = None
        while slow: #[5,6,7]2. 翻转后半部分 (从 slow.next 开始)
            temp = slow.next
            slow.next = pre
            pre = slow
            slow = temp
        first, second = head, pre# 3. 合并两部分
        while first and second:
            temp1, temp2 = first.next, second.next
            if temp1 is None: #❕
                break
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        if first: #❕
            first.next = None
