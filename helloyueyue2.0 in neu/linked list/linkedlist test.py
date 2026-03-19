#Manualy linking nodes:
'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = Node(10)
node1 = Node(20)
node2 = Node(50)
head.next = node1
node1.next = node2



'''
while head:
    print(head.data, end = "->")
    head = head.next
print("None")
'''
#creating from a list of values
nums = [10, 20, 50]
head = Node(nums[0])
current = head
for num in nums[1:]:
    new_node = Node(num)
    current.next = new_node
    current = current.next

current = head
while current:
    print(current.data, end = "->")
    current = current.next
print("None")

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        else:
            current = self.head
            while current.next: #[10,20,50]
                current = current.next #traverse to the last node
            current.next = new_node

    def prepend(self, data):
        """在链表开头插入节点"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if not self.head:
            return
        elif self.head.data == data:
            self.head = self.head.next
        else:
            current = self.head
            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                else:
                    current = current.next
  #current 其实是当前节点的“前一个节点”，通过它去“删除它后面的节点”。