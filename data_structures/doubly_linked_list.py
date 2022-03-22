class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def size(self):
        return self._size

    def push(self, value):
        """adds element to the beginning

        :param value:
        :return:
        """
        node = Node(value) # node
        node.next = self.head # node next is head
        if self.head is not None: # is head is not None head prev = node
            self.head.prev = node
        self.head = node # head = node
        self._size += 1

    def insert_at(self, index, value):
        if index > self.size() or index < 0:
            raise IndexError("Wrong index")
        if index == 0:
            self.push(value)
            return
        node = Node(value)
        current = self.head
        while index - 1 > 0:
            current = current.next
            index -= 1
        node.prev = current
        node.next = current.next
        current.next = node
        self._size +=1

    def append(self, value):
        node = Node(value)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
        node.prev = curr
        self._size+=1

    def delete_first(self):
        if self.size() == 0:
            raise Exception("DLL is empty")
        elif self.size() == 1:
            self.head = None
            self._size -=1
        else:
            self.head = self.head.next
            self.head.prev = None
            self._size-=1

    def delete_last(self):
        if self.size() == 0:
            raise Exception("DLL is empty")
        current = self.head
        while current.next:
            current = current.next
        current.prev.next = None
        self._size -=1

    def delete_at(self, index):
        if index < 0 or index >= self.size():
            raise IndexError("Wrong index")
        if index == 0:
            self.delete_first()
            return
        elif index == self.size()-1:
            self.delete_last()
            return
        current = self.head
        while index > 0:
            current = current.next
            index -= 1
        current.prev.next = current.next
        current.next.prev = current.prev
        self._size-=1
        
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __repr__(self):
        if self.head is None:
            return "Empty"
        curr = self.head
        res = [f"HEAD {curr.data} "]
        curr = curr.next
        while curr:
            res.append(f" {curr.data} ")
            curr = curr.next
        return "->".join(res)

dll = DoublyLinkedList()
dll.push(10)
dll.push(11)
dll.insert_at(0, 12)
dll.insert_at(3,13)
dll.insert_at(4,14)
dll.append(15)

print(dll)
dll.delete_at(4)
print(dll)