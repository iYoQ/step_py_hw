class Queue():
    def __init__(self):
        self.elems = []

    def enqueue(self, data):
        self.elems.insert(0, data)

    def pick(self):
        return self.elems[-1]

    def dequeue(self):
        return self.elems.pop()

    def is_empty(self):
        return len(self.elems) == 0

class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def append_left(self, data):
        self.left = Node(data)

    def append_right(self, data):
        self.right = Node(data)


class BinaryTree():
    def __init__(self, data):
        self.root = Node(data)

    def pre_traverse_print(self, node, info):
        if node:
            info += str(node.data) + '-'
            info = self.pre_traverse_print(node.left, info)
            info = self.pre_traverse_print(node.right, info)
        return info

    def in_traverse_print(self, node, info):
        if node:
            info = self.in_traverse_print(node.left, info)
            info += str(node.data) + '-'
            info = self.in_traverse_print(node.right, info)
        return info

    def post_traverse_print(self, node, info):
        if node:
            info = self.post_traverse_print(node.left, info)
            info = self.post_traverse_print(node.right, info)
            info += str(node.data) + '-'
        return info

    def breadth_first_traversal(self):
        self.__breadth('view')

    def find(self, data):
        return self.__breadth('find', data)

    def findall(self, data):
        return self.__breadth('findall', data)

    def __breadth(self, func:str, data=None):
        find_lst = []
        q = Queue()
        q.enqueue(self.root)

        while not q.is_empty():
            srch = q.pick()

            if func == 'view':
                print(srch.data, end='-')

            if func == 'find' and srch.data == data:
                return srch

            if func == 'findall' and srch.data == data:
                find_lst.append(srch)

            node = q.dequeue()

            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)

        return find_lst
