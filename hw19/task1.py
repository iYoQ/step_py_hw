class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class BidirectionList():
    def __init__(self, head:Node=None):
        self.__head = head
        self.__tail = head
        self.count = 0 if not self.__head else 1

    def view(self):
        cur_node = self.__head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if not self.__head:
            self.__head = new_node
            self.__tail = new_node
            self.count += 1
            return

        cur_node = self.__tail
        cur_node.next = new_node
        new_node.prev = cur_node
        self.__tail = new_node

        self.count += 1

    def append_begin(self, data):
        new_node = Node(data)
        new_node.next = self.__head
        new_node.next.prev = new_node
        self.__head = new_node
        self.count += 1

    def insert(self, data, index:int):
        new_node = Node(data)

        if index <= 0:
            return self.append_begin(data)

        if index >= self.count:
            return self.append(data)

        if index <= self.count // 2:
            cur_node = self.__head

            for _ in range(index-1):
                cur_node = cur_node.next

            new_node.next = cur_node.next
            new_node.next.prev = new_node
            cur_node.next = new_node
            new_node.prev = cur_node

        else:
            cur_node = self.__tail

            for _ in range(self.count-1, index, -1):
                cur_node = cur_node.prev

            new_node.prev = cur_node.prev
            cur_node.prev.next = new_node
            new_node.next = cur_node
            cur_node.prev = new_node

        self.count += 1

    def remove_end(self):
        cur_node = self.__tail
        self.__tail = cur_node.prev
        cur_node.prev.next = None

        self.count -= 1

    def remove_begin(self):
        cur_node = self.__head
        self.__head = cur_node.next
        cur_node.next.prev = None

        self.count -= 1

    def remove(self, index:int):
        if index <= 0:
            return self.remove_begin()

        if index >= self.count-1:
            return self.remove_end()

        if index <= self.count // 2:
            cur_node = self.__head

            for _ in range(index-1):
                cur_node = cur_node.next
            cur_node.next = cur_node.next.next
            cur_node.next.next.prev = cur_node

        else:
            cur_node = self.__tail

            for _ in range(self.count-1, index+1, -1):
                cur_node = cur_node.prev
            cur_node.prev.prev.next = cur_node
            cur_node.prev = cur_node.prev.prev

        self.count -= 1

    def __str__(self):
        def _print(head):
            cur_node = head
            result = '['
            while cur_node:
                result += str(cur_node.data)
                if cur_node.next:
                    result += ', '
                cur_node = cur_node.next
            return result + ']'

        return _print(self.__head)


    def __getitem__(self, index:int):
        if index >= self.count or index < 0:
            return 'bad index value'

        if index <= self.count // 2:
            cur_node = self.__head
            for _ in range(index):
                cur_node = cur_node.next

        else:
            cur_node = self.__tail
            for _ in range(self.count-1, index, -1):
                cur_node = cur_node.prev

        return cur_node.data

    def __setitem__(self, index:int, value):
        if index >= self.count or index < 0:
            print('bad index value')

        if index <= self.count // 2:
            cur_node = self.__head
            for _ in range(index):
                cur_node = cur_node.next

        else:
            cur_node = self.__tail
            for _ in range(self.count-1, index, -1):
                cur_node = cur_node.prev

        cur_node.data = value

    def __len__(self):
        return self.count

    def __bool__(self):
        return self.count > 0

    def __add__(self, llst):
        cur_node_first = self.__head
        cur_node_sec = llst.__head
        tmp_list = BidirectionList()

        while cur_node_first or cur_node_sec:
            if not cur_node_first and cur_node_sec:
                tmp_list.append(cur_node_sec.data)
                cur_node_sec = cur_node_sec.next
                continue

            if not cur_node_sec and cur_node_first:
                tmp_list.append(cur_node_first.data)
                cur_node_first = cur_node_first.next
                continue

            tmp_list.append(cur_node_first.data + cur_node_sec.data)
            cur_node_first = cur_node_first.next
            cur_node_sec = cur_node_sec.next

        return tmp_list
