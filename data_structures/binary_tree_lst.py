class BinaryTree:
    def __init__(self, max_size):
        self.custom_list = [None] * max_size
        self.last_index = 0
        self.max_size = max_size

    def insert(self, data):
        if self.last_index +1 == self.max_size:
            raise Exception("Binary Tree is full")
        self.custom_list[self.last_index+1] = data
        self.last_index+=1

    def check_item_in_tree(self, data):
        for i in range(1, self.last_index+1):
            if self.custom_list[i] == data:
                return True
        return False

    def pre_order_traversal(self, index=1):
        if index > self.last_index:
            return
        print(self.custom_list[index])
        self.pre_order_traversal(index*2)
        self.pre_order_traversal(index*2+1)

    def in_order_traversal(self, index=1):
        if index > self.last_index:
            return
        self.pre_order_traversal(index*2)
        print(self.custom_list[index])
        self.pre_order_traversal(index*2+1)

    def post_order_traversal(self, index=1):
        if index > self.last_index:
            return
        self.pre_order_traversal(index*2)
        self.pre_order_traversal(index*2+1)
        print(self.custom_list[index])

    def level_order_traversal(self):
        for i in range(1, self.last_index+1):
            print(self.custom_list[i])



bt = BinaryTree(10)
bt.insert(10)
bt.insert(11)
bt.insert(12)
bt.insert(13)
bt.insert(14)
bt.level_order_traversal()