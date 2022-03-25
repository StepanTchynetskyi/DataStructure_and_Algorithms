class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def pre_order_traversal(self):
        if self is None:
            return
        print(self.data)
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def in_order_traversal(self):
        if self is None:
            return
        if self.left:
            self.left.pre_order_traversal()
        print(self.data)
        if self.right:
            self.right.pre_order_traversal()

    def post_order_traversal(self):
        if self is None:
            return
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()
        print(self.data)

    @classmethod
    def get_height(cls, root_node):
        if not root_node:
            return 0
        return root_node.height

    def right_rotation(self):
        new_node = self.left
        self.left = self.left.right
        new_node.right = self
        self.height = 1 + max(TreeNode.get_height(self.left), TreeNode.get_height(self.right))
        new_node.height = 1 + max(TreeNode.get_height(new_node.left), TreeNode.get_height(new_node.right))
        return new_node

    def left_rotation(self):
        new_node = self.right
        self.right = self.right.left
        new_node.right = self
        self.height = 1 + max(TreeNode.get_height(self.left), TreeNode.get_height(self.right))
        new_node.height = 1 + max(TreeNode.get_height(new_node.left), TreeNode.get_height(new_node.right))
        return new_node

    def get_balance(self):
        return TreeNode.get_height(self.left) - TreeNode.get_height(self.right)

    @classmethod
    def insert(cls, root_node, data):
        if not root_node:
            return TreeNode(data)
        if data < root_node.data:
            root_node.left = cls.insert(root_node.left, data)
        else:
            root_node.right = cls.insert(root_node.right, data)

        root_node.height = 1 + max(TreeNode.get_height(root_node.left), TreeNode.get_height(root_node.right))
        balance = root_node.get_balance()
        if balance > 1 and data < root_node.left.data:
            return root_node.right_rotation()
        if balance > 1 and data > root_node.left.data:
            root_node.left = root_node.left.left_rotation()
            return root_node.right_rotation()
        if balance < -1 and data > root_node.right.data:
            return root_node.left_rotation()
        if balance < -1 and data < root_node.right.data:
            root_node.right = root_node.right.right_rotation()
            return root_node.left_rotation()
        return root_node

    @classmethod
    def get_min_value(cls, root_node):
        if root_node is None or root_node.left is None:
            return root_node
        return cls.get_min_value(root_node.left)

    @classmethod
    def delete_node(cls, root_node, data):
        if not root_node:
            return root_node
        if data < root_node.data:
            root_node.left = TreeNode.delete_node(root_node.left, data)
        elif data > root_node.data:
            root_node.right = TreeNode.delete_node(root_node.right, data)
        else:
            if root_node.left is None:
                temp = root_node.right
                root_node = None
                return temp
            elif root_node.right is None:
                temp = root_node.left
                root_node = None
                return temp
            temp = TreeNode.get_min_value(root_node.right)
            root_node.data = temp.data
            root_node.right = TreeNode.delete_node(root_node.right, temp.data)
            balance = TreeNode.get_balance(root_node)
            if balance > 1 and TreeNode.get_balance(root_node.left) >=0:
                return root_node.right_rotation()
            if balance < -1 and TreeNode.get_balance(root_node.right) <=0:
                return root_node.left_rotation()
            if balance > 1 and TreeNode.get_balance(root_node.left) < 0:
                root_node.left = root_node.left.left_rotation()
                return root_node.right_rotation()
            if balance < -1 and TreeNode.get_balance(root_node.left) > 0:
                root_node.right = root_node.right.right_rotation()
                return root_node.left_rotation()
            return root_node
    def __repr__(self):
        return f"id={id(self)}, data={self.data}"

if __name__ == "__main__":
    root = TreeNode(10)
    l = TreeNode(9)
    r = TreeNode(11)
    ll = TreeNode(8)
    lr = TreeNode(9.5)

    root.left = l
    root.right = r
    l.left = ll
    TreeNode.insert(root, 7)
    root.pre_order_traversal()