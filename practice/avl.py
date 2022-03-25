class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    @classmethod
    def pre_order_traversal(cls, root):
        if root is None:
            return root
        print(root.data)
        cls.pre_order_traversal(root.left)
        cls.pre_order_traversal(root.right)

    @classmethod
    def in_order_traversal(cls, root):
        if root is None:
            return root
        cls.in_order_traversal(root.left)
        print(root.data)
        cls.in_order_traversal(root.right)

    @classmethod
    def post_order_traversal(cls, root):
        if root is None:
            return root
        cls.in_order_traversal(root.left)
        cls.in_order_traversal(root.right)
        print(root.data)

    @classmethod
    def get_height(cls, root):
        if root is None:
            return 0
        return root.height

    def get_balance(self):
        return TreeNode.get_height(self.left) - TreeNode.get_height(self.right)

    @classmethod
    def right_rotation(cls, root):
        new_node = root.left
        root.left = root.left.right
        new_node.right = root
        root.height = TreeNode.reset_height(root)
        new_node.height = TreeNode.reset_height(new_node)
        return new_node

    @classmethod
    def left_rotation(cls, root):
        new_node = root.right
        root.right = root.right.left
        new_node.left = root
        root.height = TreeNode.reset_height(root)
        new_node.height = TreeNode.reset_height(new_node)
        return new_node

    @classmethod
    def reset_height(cls, root):
        return 1 + max(TreeNode.get_height(root.left), TreeNode.get_height(root.right))

    @classmethod
    def insert(cls, root, data):
        if root is None:
            return TreeNode(data)
        if data < root.data:
            root.left = TreeNode.insert(root.left, data)
        else:
            root.right = TreeNode.insert(root.right, data)
        root.height = TreeNode.reset_height(root)
        balance = TreeNode.get_balance(root)
        if balance > 1 and data < root.data:
            return TreeNode.right_rotation(root)
        if balance > 1 and data > root.data:
            root.left = TreeNode.left_rotation(root.left)
            return TreeNode.right_rotation(root)
        if balance < -1 and data > root.data:
            return TreeNode.left_rotation(root)
        if balance < -1 and data < root.data:
            root.right = TreeNode.right_rotation(root.right)
            return TreeNode.left_rotation(root)
        return root
    @classmethod
    def get_min_node(cls, root):
        if root is None or root.left is None:
            return root
        return TreeNode.get_min_node(root.left)
    @classmethod
    def delete_node(cls, root, data):
        if root is None:
            return root
        if data < root.data:
            root.left = TreeNode.delete_node(root.left, data)
        elif data > root.data:
            root.right = TreeNode.delete_node(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            if root.right is None:
                temp = root.left
                root = None
                return temp
            temp = TreeNode.get_min_node(root.right)
            root.data = temp.data
            root.right = TreeNode.delete_node(root.right, temp.data)
            balance = TreeNode.get_balance(root)
            if balance > 1 and TreeNode.get_balance(root.left) >=0:
                return TreeNode.right_rotation(root)
            if balance > 1 and TreeNode.get_balance(root.left) < 0:
                root.left = TreeNode.left_rotation(root.left)
                return TreeNode.right_rotation(root)
            if balance < -1 and TreeNode.get_balance(root.right)<=0:
                return TreeNode.left_rotation(root)
            if balance < -1 and TreeNode.get_balance(root.right)>0:
                root.right = TreeNode.right_rotation(root.right)
                return TreeNode.left_rotation(root)
            return root



t = TreeNode(10)
TreeNode.insert(t, 11)
TreeNode.insert(t, 9)
TreeNode.insert(t, 8)
TreeNode.insert(t, 7)

TreeNode.pre_order_traversal(t)
