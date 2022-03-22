class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data <= self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def min_value(self):
        current =self
        while current.left is not None:
            current = current.left
        return current

    def delete_node(self, data):
        if self.data is None:
            return self
        if data < self.data:
            self.left = self.left.delete_node(data)
        elif data > self.data:
            self.right = self.right.delete_node(data)
        else:
            if self.right is None:
                temp = self.left
                self = None
                return temp
            elif self.left is None:
                temp = self.right
                self = None
                return temp
            temp = self.right.min_value()
            print(temp)
            self.data = temp.data
            self.right = self.right.delete_node(temp.data)
        return self

    def search(self, data):
        if self.data == data:
            return True
        elif data < self.data:
            self.left.search(data)
        else:
            self.right.search(data)
        return False

    def __str__(self, level = 0):
        ret = "   " * level + repr(self.data) + "\n"
        for child in [self.left, self.right]:
            if child:
                ret += child.__str__(level + 1)
        return ret

root = TreeNode(100)
root.insert(90)
root.insert(110)
root.insert(80)
root.insert(95)
root.insert(97)
root.insert(93)
root.insert(92)
root.insert(94)
root.insert(96)
root.insert(98)
# root.delete_node(95)
print(root.search(1000))