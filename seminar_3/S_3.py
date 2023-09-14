class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __str__(self):
        return f"{self.data} -> {self.next_node}"


class LinkedList:

    def __init__(self, data):
        self.head = self.Node(data)
        self.length = 1

    def __str__(self):
        return f"{self.head}"

    def find_last(self):
        cur_node = self.head
        if cur_node is None:
            return None
        while cur_node.next_node:
            cur_node = cur_node.next_node
        return cur_node

    def append(self, data):
        node = self.Node(data)
        last_node = self.find_last()
        if last_node is None:
            self.head = node
        else:
            last_node.next_node = node
        self.length += 1

    def insert_head(self, data):
        node = self.Node(data)
        if self.head:
            node.next_node = self.head
        self.head = node
        self.length += 1

    def del_last(self):
        if self.head is None:
            return
        cur_node = self.head
        if cur_node.next_node is None:
            self.head = None
        else:
            while cur_node.next_node.next_node:
                cur_node = cur_node.next_node
            cur_node.next_node = None
        self.length -= 1

    def del_head(self):
        if self.head is None:
            return
        self.head = self.head.next_node
        self.length -= 1

    def find_data(self, data):
        if self.head is None:
            return False
        cur_node = self.head
        while cur_node:
            if cur_node.data == data:
                return True
            cur_node = cur_node.next_node
        return False

    # def get_length(self):
    #     cur_node = self.head
    #     count = 0
    #     while cur_node:
    #         count += 1
    #         cur_node = cur_node.next_node
    #     return count

    def insert_into(self, index, data):
        cur_node = self.head
        if not isinstance(index, int):
            raise ValueError('Введите число')
        if index < 1 or index > self.length + 1:
            raise ValueError(f'Длина списка составляет {self.length}. \nВведите корректное число.')
        if index == 1:
            return self.insert_head(data)
        count = 1
        while count < index - 1:
            cur_node = cur_node.next_node
            count += 1
        node = self.Node(data)
        next_node = cur_node.next_node
        cur_node.next_node = node
        node.next_node = next_node
        self.length += 1

    # def put(self, value):
    #     """Добавление в конец списка"""
    #     el = self.head
    #     if el is None:
    #         self.head = self.Node(value)
    #         return
    #     while el.next is not None:
    #         el = el.next
    #     el.next = self.Node(value)
