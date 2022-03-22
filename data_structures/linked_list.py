class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def __repr__(self):
        nodes = []
        current = self.head
        if self.size() == 0:
            return "Empty LinkedList"
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return f'LinkedList(size={self.size()})' + '-> '.join(nodes)

    def size(self):
        return self.count

    def resize(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next_node
        self.count = count

    def is_empty(self):
        return self.head is None

    def add(self, data):
        node = Node(data, next_node=self.head)
        self.head = node
        self.count += 1

    def get_node_by_index(self, index):
        if self.count <= index:
            raise IndexError('index out of range')
        if index == 0:
            return self.head
        current = self.head
        position = 0
        while position < index:
            current = current.next_node
            position += 1
        return current

    def _split(self):
        if self is None or self.head is None:
            left_half = self
            right_half = None
        else:
            mid = self.size() // 2 - 1
            mid_node = self.get_node_by_index(mid)

            left_half = self
            left_half.count = mid + 1
            right_half = LinkedList()
            right_half.head = mid_node.next_node
            right_half.count = self.size() - mid + 1
            mid_node.next_node = None

        return left_half, right_half

    def _merge(self, right_half):
        left_half = self.head
        right_half = right_half.head
        sorted = LinkedList()
        sorted.add(0)  # temp head
        current = sorted.head
        while left_half is not None or right_half is not None:
            if right_half is None:
                current.next_node = left_half
                left_half = left_half.next_node
            elif left_half is None:
                current.next_node = right_half
                right_half = right_half.next_node
            else:
                if left_half.data < right_half.data:
                    current.next_node = left_half
                    left_half = left_half.next_node
                else:
                    current.next_node = right_half
                    right_half = right_half.next_node
            current = current.next_node
        head = sorted.head.next_node
        sorted.head = head
        return sorted

    def merge_sort(self):
        if self.size() == 1 or self.head is None:
            return self
        left_half, right_half = self._split()
        left_half = left_half.merge_sort()
        right_half = right_half.merge_sort()
        return left_half._merge(right_half)


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


