class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)

        cur = len(self.items)-1
        while cur>=2 and self.items[cur] > self.items[cur//2]:
            self.items[cur], self.items[cur//2], cur = self.items[cur//2], self.items[cur], cur//2

max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!