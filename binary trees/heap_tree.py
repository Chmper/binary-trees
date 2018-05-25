class HEAP_tree:
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

        def __repr__(self):
            return str(self.value)

        def overwrite(self, node):
            self.parent = node.parent
            self.left = node.left
            self.right = node.right
            self.value = node.value
            self.is_right = node.is_right
            self.is_left = node.is_left

    def __init__(self):
        self.currentSize = 0
        self.heapList = []

    def insert(self, x):
        node = self.Node(x)
        self.heapList.append(node)
        self.currentSize += 1

        if self.currentSize > 1: # 2->1  3->1  4->2  5->2  5->3
            parent = self.heapList[self.currentSize//2-1]
            node.parent = parent

            if parent.left is None:
                parent.left = node
                node.is_left = True
            else:
                parent.right = node
                node.is_right = True

            i = self.currentSize

            while i//2 > 0:
                if node.value < node.parent.value:
                    temp = node.parent.value
                    node.parent.value = node.value
                    node.value = temp
                i = i//2
                node = node.parent


    def pre_order_print(self, root):
        if not root:
            return
        print (root.value)
        self.pre_order_print(root.left)
        self.pre_order_print(root.right)


    def find_max(self, node):
        current = node

        while current.right is not None:
            current = current.right
        return current

    def find(self, x):
        for h in self.heapList:
            if h.value == x:
                return h
        return None

    def min(self, node):
        try:
            if node.left.value > node.right.value:
                return node.right
            else:
                return node.left
        except AttributeError:
            if node.left:
                return node.left
            else:
                return node.right

    def delete(self, x):
        temp = self.find(x)

        if temp.left == None and temp.right == None:
            temp.value = self.heapList[-1].value
            self.heapList.pop()
            while temp.value < temp.parent.value:
                pom = temp.parent
                pom2 = temp.parent.value
                temp.parent.value = temp.value
                temp.value = pom2

                temp = pom

        elif temp.left != None and temp.right != None:
            temp.value = self.heapList[-1].value
            self.heapList.pop()

            compare = self.min(temp)

            if temp.value > compare.value:
                pom = compare
                pom2 = compare.value
                compare.value = temp.value
                temp.value = pom2

                temp = compare
                compare = self.min(compare)

        else:
            temp = self.heapList[-1]
            self.heapList.pop()

            while temp.parent.value < temp.value:
                pom = temp.parent
                temp.parent.value = temp.value
                temp.value = pom.value

                temp = pom.parent
                if temp is None:
                    break



if __name__ == '__main__':
    heap = HEAP_tree()
    heap.insert(40)
    heap.insert(10)
    heap.insert(25)
    heap.insert(9)
    heap.insert(8)
    heap.insert(16)
    heap.insert(82)
    heap.insert(33)
    heap.insert(2)
    heap.insert(15)
    heap.insert(30)
    heap.insert(19)
    heap.pre_order_print(heap.heapList[0])
    heap.delete(16)
    #heap.pre_order_print(heap.heapList[0])
    print(heap.heapList)
