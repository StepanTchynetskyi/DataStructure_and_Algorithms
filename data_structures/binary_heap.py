class BinaryHeap:
    def __init__(self, max_size, heap_type="min"):
        self.storage = (max_size + 1) * [None]
        self.heap_size = 0
        self.max_size = max_size + 1
        self.heap_type = heap_type.lower()

    def peek_of_heap(self):
        return self.storage[1]

    def size(self):
        return self.heap_size

    def level_order_traversal(self):
        for i in range(1, self.heap_size + 1):
            print(self.storage[i])

    def resize(self):
        self.storage.extend(self.max_size * [None])
        self.max_size = self.max_size * 2

    def heapify_tree_insert(self, index):
        parent_index = index // 2
        if index <= 1:
            return
        if self.heap_type == "min":
            if self.storage[index] < self.storage[parent_index]:
                self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
            self.heapify_tree_insert(parent_index)
        elif self.heap_type == "max":
            if self.storage[index] > self.storage[parent_index]:
                self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
            self.heapify_tree_insert(parent_index)

    def insert(self, data):
        if self.heap_size + 1 == self.max_size:
            self.resize()
        self.storage[self.heap_size + 1] = data
        self.heap_size += 1
        self.heapify_tree_insert(self.heap_size)

    def heapify_tree_extract(self, index):
        left_index = index * 2
        right_index = index * 2 + 1
        if self.heap_size < left_index:
            return
        elif self.heap_size == left_index:
            if self.heap_type == "min":
                if self.storage[index] > self.storage[left_index]:
                    self.storage[index], self.storage[left_index] = self.storage[left_index], self.storage[index]
                return
            else:
                if self.storage[index]< self.storage[left_index]:
                    self.storage[index], self.storage[left_index] = self.storage[left_index], self.storage[index]
                return
        else:
            if self.storage[left_index] > self.storage[right_index]:
                swap = left_index
            else:
                swap = right_index
            if self.storage[index] < self.storage[swap]:
                self.storage[index], self.storage[swap] = self.storage[swap], self.storage[index]
            self.heapify_tree_insert(swap)

    def extract_node(self):
        if self.heap_size==0:
            return
        else:
            extracted_node = self.storage[1]
            self.storage[1] = self.storage[self.heap_size]
            self.storage[self.heap_size] = None
            self.heap_size-=1
            return extracted_node


if __name__ == "__main__":
    bh = BinaryHeap(5)
    bh.insert(10)
    bh.insert(11)
    bh.insert(5)
    bh.insert(4)
    bh.level_order_traversal()
