class AVL_tree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.parent = None
            self.left = None
            self.right = None
            self.is_right = False
            self.is_left = False

        def __str__(self):
            return str(self.value)

        @property
        def grandpa(self):
            if self.parent:
                return self.parent.parent
            else:
                return None

        @property
        def balance(self):
            rh = self.right.height if self.right else 0
            lh = self.left.height if self.left else 0

            return rh - lh

        @property
        def height(self):
            lh = self.left.height if self.left else 0
            rh = self.right.height if self.right else 0
            if lh > rh:
                return lh + 1
            else:
                return rh + 1

        def _balance(self, root):
            if self.balance > 1:
                if self.right.balance < 0:
                    self.rl_rotate(root)
                elif self.right.balance > 0:
                    self.rr_rotate(root)
            elif self.balance < -1:
                if self.left.balance < 0:
                    self.ll_rotate(root)
                elif self.left.balance > 0:
                    self.lr_rotate(root)

        def ll_rotate(self, root):
            child = self.left

            if self is root or self.value > self.parent.value:
                self.parent.right = child
            else:
                self.parent.left = child

            child.parent, self.parent = self.parent, child
            child.right, self.left = self, child.right

        def rr_rotate(self, root):
            child = self.right

            if self is root or self.value > self.parent.value:
                self.parent.right = child
            else:
                self.parent.left = child

            child.parent, self.parent = self.parent, child
            child.left, self.right = self, child.left

        def lr_rotate(self, root):
            child, grand_child = self.left, self.left.right
            child.parent, grand_child.parent = grand_child, self
            child.right = grand_child.left
            self.left, grand_child.left = grand_child, child
            self.ll_rotate(root)

        def rl_rotate(self, root):
            child, grand_child = self.right, self.right.left
            child.parent, grand_child.parent = grand_child, self
            child.left = grand_child.right
            self.right, grand_child.right = grand_child, child
            self._rr_case(root)


    def __init__(self):
        self.root = None

    def insert(self, x, root = None):
        if root is None:
            root = self.root

        if self.root is None:
            self.root = self.Node(x)

        else:
            temp = self.Node(x)
            if root.value > temp.value:
                if root.left is None:
                    root.left = temp
                    temp.parent = root
                    temp.is_left = True
                    self.balance_grandpa(temp)
                else:
                    self.insert(x, root.left)
            else:
                if root.right is None:
                    root.right = temp
                    temp.parent = root
                    temp.is_right = True
                    self.balance_grandpa(temp)
                else:
                    self.insert(x, root.right)

    def balance_grandpa(self, node):
        if node.grandpa and self.root == node.grandpa:
            pass
        elif node.grandpa and not self.root is node.grandpa:
            node.grandpa._balance(self.root)
        elif node.grandpa is None:
            pass
        else:
            raise NotImplementedError
        return

    def pre_order_print(self, root):
        if not root:
            return
        print (root.value)
        self.pre_order_print(root.left)
        self.pre_order_print(root.right)

    def find(self, x):
        temp = self.root
        while temp != None:
            if temp.value == x:
                return temp
            elif x > temp.value:
                temp = temp.right
            else:
                temp = temp.left
        return None

    def find_max(self, node):
        current = node

        while current.right is not None:
            current = current.right
        return current




if __name__ == '__main__':
    avl = AVL_tree()
    values = [50, 40, 60, 30, 20, 56, 59]
    for v in values:
        avl.insert(v)

    print('find:', avl.find(50))
    print('find:', avl.find(10))
    ## BRAK FUNKCJI USUWANIA ELEMENTOW ##
    avl.pre_order_print(avl.root)
