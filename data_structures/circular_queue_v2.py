class CircularQueue:
    def __init__(self, max_size):
        self.head = -1
        self.tail = -1
        self.max_size = max_size
        self.queue = [None] * max_size

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return (self.tail+1) % self.max_size == self.head

    def enqueue(self, data):
        if self.is_full():
            raise Exception("CircularQueue is full")
        if self.head==-1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.max_size
            self.queue[self.tail] = data

    def dequeue(self):
        if self.is_empty():
            raise Exception("CircularQueue is empty")
        elif self.head == self.tail:
            data = self.queue[self.head]
            self.queue[self.head] = None
            self.head = -1
            self.tail = -1
        else:
            data = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head +1) % self.max_size
        return data

    def __repr__(self):
        if self.is_empty():
            return f"CircularQueue is empty (capacity={self.max_size})"
        size = (self.tail-self.head) % self.max_size +1
        res = [f"CircularQueue (size={size}/{self.max_size}) HEAD"]
        end = "TAIL"
        curr = self.head
        while curr != self.tail:
            res.append(str(self.queue[curr]))
            curr = (curr +1) % self.max_size
        res.append(str(self.queue[curr]))
        res.append(end)
        return "->".join(res)

q = CircularQueue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.enqueue(4)
q.dequeue()
q.dequeue()
q.enqueue(4)
q.dequeue()
q.dequeue()
print(q)