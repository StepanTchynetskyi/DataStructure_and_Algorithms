class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class QueueShelter:
    def __init__(self):
        self.head = None
        self.tail = None
        self.dog = None
        self.cat = None
        self._size = 0

    def enqueue(self, animal):
        self._size +=1
        node = Node(animal)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node


    def dequeue_any(self):
        if not self.head:
            return None
        result = self.head.value
        self.head = self.head.next_node
        self._size -= 1
        return result

    def dequeue_dog(self):
        return self._dequeue_animal("dog")

    def dequeue_cat(self):
        return self._dequeue_animal("cat")

    def _dequeue_animal(self, animal):
        if self.head is None:
            return None
        current = self.head
        while current.next_node and current.next_node.value != animal:
            current = current.next_node
        if current.next_node is None:
            return None
        result = current.next_node.value
        current.next_node = current.next_node.next_node
        self._size -= 1
        return result

    def size(self):
        return self._size

    def __repr__(self):
        nodes = []
        current = self.head
        if self.size() == 0:
            return "Empty LinkedList"
        while current:
            if current is self.head:
                nodes.append("[Head: %s %s]" % (current.value, id(current)))
            elif current.next_node is None:
                nodes.append("[Tail: %s %s]" % (current.value, id(current)))
            else:
                nodes.append("[%s %s]" % (current.value, id(current)))
            current = current.next_node
        return f'LinkedList(size={self.size()})' + '-> '.join(nodes)

q = QueueShelter()

q.enqueue("dog")
q.enqueue("dog")
q.enqueue("cat")
q.enqueue("dog")
print(q)
q.dequeue_any()
print(q)
q.dequeue_cat()
print(q)
q.dequeue_cat()
print(q)