class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        print(cur.data)
        while cur.next is not None:
            cur = cur.next
            print(cur.data)
            

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(12)
linked_list.append(12)
linked_list.print_all()