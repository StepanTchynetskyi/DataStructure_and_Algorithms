class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class CircularQueue:
    def __init__(self, max_size):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self.max_size

    def enqueue(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next_node = self.head
            self.tail = self.head
        elif self.is_full():
            raise Exception("CircularQueue is full")
        else:
            node.next_node = self.head
            self.tail.next_node = node
            self.tail = node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("CircularQueue is empty")
        else:
            node = self.head
            self.head = self.head.next_node
            self.tail.next_node = self.head
            self._size-=1
            return node

    def __repr__(self):
        if self.is_empty():
            return "CircularQueue is empty"
        curr = self.head
        res = [str(curr.data)]
        while curr.next_node is not self.head:
            curr = curr.next_node
            res.append(str(curr.data))
        res.insert(0, f"CircularQueue (size={self._size}/{self.max_size}) HEAD")
        res.append("TAIL")
        res = "->".join(res)
        return res

    def __iter__(self):
        curr =self.head
        while curr:
            yield curr.data
            curr = curr.next_node

q = CircularQueue(10)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(next(q))
print(q)


