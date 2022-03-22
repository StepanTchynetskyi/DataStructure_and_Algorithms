from custom_queue import Queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if self.data == None:
            self.data = data
            return
        node = TreeNode(data)
        customQueue = Queue()
        customQueue.enqueue(self)
        while not (customQueue.is_empty()):
            root = customQueue.dequeue()
            if root.data.left is not None:
                customQueue.enqueue(root.data.left)
            else:
                root.data.left = node
                return
            if root.data.right is not None:
                customQueue.enqueue(root.data.right)
            else:
                root.data.right = node
                return

    def delete_node(self, data):
        if self.data == data:
            self.data = None
            self.right = None
            self.left = None
        customQueue = Queue()
        customQueue.enqueue(self)
        while not (customQueue.is_empty()):
            root = customQueue.dequeue()
            if root.data.left and root.data.left.data == data:
                root.data.left = None
                return
            elif root.data.right and root.data.right.data == data:
                root.data.right = None
                return
            if root.data.left is not None:
                customQueue.enqueue(root.data.left)
            if root.data.right is not None:
                customQueue.enqueue(root.data.right)
        return -1

    def __str__(self, level=0):
        ret = "   " * level + repr(self.data) + "\n"
        for child in [self.left, self.right]:
            if child:
                ret += child.__str__(level + 1)
        return ret


def pre_order_traversal_lst(root):
    if not root:
        return []
    return [root.data] + pre_order_traversal_lst(root.left) + pre_order_traversal_lst(root.right)


def pre_order_traversal(root):
    if not root:
        return
    print(root.data)
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)


def in_order_traversal(root):
    if not root:
        return
    in_order_traversal(root.left)
    print(root.data)
    in_order_traversal(root.right)


def post_order_traversal(root):
    if not root:
        return
    in_order_traversal(root.left)
    in_order_traversal(root.right)
    print(root.data)


def level_order_traversal(root):
    if not root:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(root)
        while not customQueue.is_empty():
            root = customQueue.dequeue()
            print(root.data.data)
            if root.data.left:
                customQueue.enqueue(root.data.left)
            if root.data.right:
                customQueue.enqueue(root.data.right)


t = TreeNode(10)
t.insert(13)
t.insert(12)
t.insert(1)
t.insert(2)
# t.delete_node(10)
# t.insert(6)
print(t)
# print(pre_order_traversal(t))
level_order_traversal(t)