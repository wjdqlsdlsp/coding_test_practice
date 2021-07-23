class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        tmp = self.head
        self.head = self.head.next
        return tmp

    def peek(self):
        if self.is_empty():
            return "Stack is Empty"        
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        if self.head is None:
            return True
        return False

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
a = stack.pop()
print(a.data)

a = stack.pop()
print(a.data)

a = stack.pop()
print(a.data)

print(stack.peek())
print(stack.peek())
print(stack.peek())
