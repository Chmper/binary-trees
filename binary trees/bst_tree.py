import random

class BST_tree:
    class Node:
        def __init__(self, x=0):
            self.parent = None
            self.left = None
            self.right = None
            self.value = x
            self.is_right = False
            self.is_left = False

        def __str__(self):
            return 'value: '+ str(self.value)

        def overwrite(self, node):
            self.parent = node.parent
            self.left = node.left
            self.right = node.right
            self.value = node.value
            self.is_right = node.is_right
            self.is_left = node.is_left

    def __init__(self):
        self.root = None

    def add(self, x, root = None):
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
                else:
                    self.add(x, root.left)
            else:
                if root.right is None:
                    root.right = temp
                    temp.parent = root
                    temp.is_right = True
                else:
                    self.add(x, root.right)


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

    def delete(self, x):
        temp = self.find(x)

        if temp.left == None and temp.right == None:
            if temp.is_left:
                temp.parent.left = None
            else:
                temp.parent.right = None
        elif temp.left != None and temp.right != None:
            pom = self.find_max(temp.left)
            temp.overwrite(pom)

        else:
            if temp.left:
                if temp.is_left:
                    temp.parent.left = temp.left
                else:
                    temp.parent.right = temp.left
            else:
                if temp.is_left:
                    temp.parent.left = temp.right
                else:
                    temp.parent.right = temp.right


if __name__ == '__main__':
    bst = BST_tree()
    bst.add(50)
    bst.add(30)
    bst.add(70)
    bst.add(20)
    bst.add(40)
    bst.add(60)
    bst.add(80)
    bst.pre_order_print(bst.root)
    print('#'*20)
    bst.delete(70)
    bst.pre_order_print(bst.root)
