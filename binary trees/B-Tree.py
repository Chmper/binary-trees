import random

class BTree:
    class  BTree_Node:
        def __init__(self):
            self.parent = None
            self.keys = []
            self.childrens = []

        def __str__(self):
            return self.keys.__str__()

        @property
        def size(self):
            return len(self.keys)

    def __init__(self):
        self.root = self.BTree_Node()
        self.M = 4

    def find_to_insert(self, x, node = None):
        if node is None:
            node = self.root

        if len(node.childrens) == 0:
            return node
        else:
            parent = None
            while len(node.childrens) > 0:
                for i in range(node.size-1, -1, -1):
                    if x > node.keys[i]:
                        node = node.childrens[i+1]
                        break
                    if i == 0:

                        node =  node.childrens[0]

            return node

    def find_parent(self, x):
        node = self.root
        parent = None

        while len(node.childrens) > 0:
            for i in range(node.size-1, -1, -1):
                if x > node.keys[i]:
                    parent = node
                    try:
                        node = node.childrens[i+1]
                    except IndexError:
                        print('blad na:', x)
                        exit()
                    break
                if i == 0:
                    parent = node
                    node = node.childrens[0]
                    break

        return parent

    def insert(self, x):
        temp = self.find_to_insert(x)
        parent = self.find_parent(x)

        temp.keys.append(x)
        temp.keys.sort()


        if not temp.parent:
            temp.parent = parent

        if len(temp.keys) > self.M - 1:
            self.rozbicie(temp)

    def rozbicie(self, node):
        if node.parent is None:
            first = node.keys[0]
            middle = node.keys[1]
            last = node.keys[2:]

            root = self.BTree_Node()
            left = self.BTree_Node()
            right = self.BTree_Node()
            root.keys.append(middle)
            left.keys.append(first)
            right.keys = last
            root.childrens.append(left)
            root.childrens.append(right)
            left.parent = root
            right.parent = root
            self.root = root

            left.childrens = node.childrens[:2]
            right.childrens = node.childrens[2:]

            for child in node.childrens[:2]:
                child.parent = left
            for child in node.childrens[2:]:
                child.parent = right

            del node
        else:
            first = node.keys[0]
            middle = node.keys[1]
            last = node.keys[2:]

            left = self.BTree_Node()
            right = self.BTree_Node()
            node.parent.keys.append(middle)
            node.parent.keys.sort()
            left.keys.append(first)
            right.keys = last

            node.parent.childrens.append(left)
            node.parent.childrens.append(right)
            node.parent.childrens.remove(node)
            self.sort_childres(node.parent.childrens)
            left.parent = node.parent
            right.parent = node.parent

            left.childrens = node.childrens[:2]
            right.childrens = node.childrens[2:]

            for child in node.childrens[:2]:
                child.parent = left
            for child in node.childrens[2:]:
                child.parent = right

            if node.parent.size == 4:
                self.rozbicie(node.parent)

            del node

    def sort_childres(self, array):
        for i in range(len(array)):
            for j in range(len(array)-1):
                if array[j].keys[0] > array[j+1].keys[0]:
                    array[j], array[j+1] = array[j+1], array[j]

    def find_value(self, x, node = None):
        if node is None:
            node = self.root

        while node is not None:
            for i in range(node.size-1,-1,-1):
                if x in node.keys:
                    return node
                if x > node.keys[i]:
                    node = node.childrens[i+1]
                    break

                if i == 0:
                    try:
                        node = node.childrens[0]
                        break
                    except IndexError:
                        return None
        return None

    def delete(self, x):
        to_delete = self.find_value(x)

        for i in range(len(to_delete.keys)):
            if to_delete.keys[i] == x:
                break

        if len(to_delete.childrens) == 0:
            to_delete.keys.remove(x)
        else:
            to_delete.keys.remove(x)
            to_delete.keys.append(to_delete.childrens[i].keys[-1])
            to_delete.childrens[i].keys.pop()
            to_delete.keys.sort()

            if to_delete.childrens[i].size == 0:
                to_delete.childrens[i].keys.append(to_delete.keys[i-1])
                to_delete.keys.remove(to_delete.keys[i-1])
                to_delete.keys.append(to_delete.childrens[i-1].keys[-1])
                to_delete.keys.sort()
                to_delete.childrens[i-1].keys.pop()

        if to_delete.size == 0:
            for i in range(len(to_delete.parent.childrens)):
                if to_delete.parent.childrens[i] is to_delete:
                    break

            if i != 0:
                to_delete.parent.keys.append(to_delete.parent.childrens[i-1].keys[-1])
                to_delete.parent.childrens[i-1].keys.pop()
                to_delete.keys.append(to_delete.parent.keys[i-1])
                to_delete.parent.keys.remove(to_delete.parent.keys[i-1])
                to_delete.parent.keys.sort()


    def pre_order_print(self, node):
        if not node:
            return
        print(node.keys)
        for child in node.childrens:
            self.pre_order_print(child)


if __name__ == '__main__':
    btree = BTree()

    btree.insert(20)
    btree.insert(30)
    btree.insert(25)
    btree.insert(12)
    btree.insert(2)
    btree.insert(565)
    btree.insert(23)
    btree.insert(23)
    btree.insert(15)
    btree.insert(90)
    btree.insert(500)
    btree.pre_order_print(btree.root)
    print('#'*20)
    btree.delete(20)
    btree.delete(30)
    btree.delete(23)

    print('USUWANIE NIE DZIALA DO KONCA POOPRAWNIE')

    btree.pre_order_print(btree.root)
    print('#'*20)

    print('znajdz 15:')
    print(btree.find_value(15))
    print('znajdz 199:')
    print(btree.find_value(199))
