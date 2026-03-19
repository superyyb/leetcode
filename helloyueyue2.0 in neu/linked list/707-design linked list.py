class Node:
    def __init__(self, val=0, next=None):#singly linked list
        self.val = val
        self.next = next
class MyLinkedList:
    def __init__(self):
        self.dummy = Node() #规定链表head节点
        self.size = 0 #规定链表长度
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.dummy.next #从dummy后的第一个节点开始
        for i in range(index):
            curr = curr.next #遍历
        return curr.val
    def addAtHead(self, val: int) -> None:
        new_node = Node(val) #dummy->A->B 插入C
        new_node.next = self.dummy.next #C->A(A目前还是dummy.next)
        self.dummy.next = new_node #dummy->C(把dummy.next命名为指向C)
        self.size +=1
    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        curr = self.dummy
        while curr.next:
            curr = curr.next
        curr.next = new_node #curr->new_node
        self.size +=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        new_node = Node(val)
        curr = self.dummy
        for i in range(index):
            curr = curr.next
        """
        temp = curr.next        # step 1: 记住旧指针
        new_node.next = temp    # step 2: new 指向原链
        curr.next = new_node    # step 3: 插入新节点
        """
        new_node.next = curr.next #new先指向原来的curr.next
        curr.next = new_node #把curr.next改成new
        self.size +=1
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size - 1:
            return
        curr = self.dummy
        for i in range(index):
            curr = curr.next
        curr.next = curr.next.next
        self.size -= 1