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


def _get_linked_list_sum(linked_list):
    cur = linked_list.head
    if cur.next is None:
        num = cur.data
    else:
        num = cur.data
        while cur.next is not None:
            cur = cur.next
            num = num*10 + cur.data

    return num

def get_linked_list_sum(linked_list_1, linked_list_2):
    num_1 = _get_linked_list_sum(linked_list_1)
    num_2 = _get_linked_list_sum(linked_list_2)

    return num_1 + num_2


linked_list_1 = LinkedList(1)
linked_list_1.append(2)
# linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))