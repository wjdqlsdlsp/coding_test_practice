class LiknedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k,v in self.items:
            if key ==k:
                return v

class LikedDcit:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LiknedTuple())

    def put(self, key, value):
        index =hash(key) % len(self.items)
        return self.items[index].add(key,value)

    def get(self,  key):
        index =hash(key) % len(self.items)
        return self.items[index].get(key)