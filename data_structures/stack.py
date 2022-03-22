class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.head = None
        self._size = 0

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size

    def push(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            node.next_node = self.head
            self.head = node
            self._size+=1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            node = self.head
            self.head = self.head.next_node
            self._size -= 1
            return node

    def __repr__(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            curr = self.head
            res = [str(curr.data)]
            while curr.next_node:
                curr = curr.next_node
                res.append(str(curr.data))
            res = res[::-1]
            res.insert(0,"HEAD")
            res.append("TAIL")
            return "->".join(res)

s = Stack()
s.push(3)
s.push(4)
s.push(6)
s.pop()
print(s)