class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_head = Node(value)
        if self.is_empty():
            self.head = new_head
            self.tail = new_head
        else:
            self.tail.next = new_head
            self.tail = new_head

    def dequeue(self):
        if self.is_empty():
            return "queue is Empty"
        delete_head = self.head
        self.head = self.head.next

        return delete_head
        

    def peek(self):
        return self.head.data

    def is_empty(self):
        if self.head is None:
            return True
        return False
 
que = Queue()
que.enqueue(1)
que.enqueue(2)
print(que.dequeue().data)
print(que.dequeue().data)

que.enqueue(1)
print(que.peek())

