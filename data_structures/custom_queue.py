class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        return self.head is None
    def enqueue(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next_node = node
            self.tail = self.tail.next_node
        self._size +=1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            node = self.head
            self.head = self.head.next_node
            self._size -= 1
            return node

    def size(self):
        return self._size

    def __repr__(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            curr = self.head
            res = ["HEAD",str(self.head.data)]
            while curr.next_node:
                curr = curr.next_node
                res.append(str(curr.data))
            res.append("TAIL")
            return "->".join(res)

# q = Queue()
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)
# q.dequeue()
# print(q)