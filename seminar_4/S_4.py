# Задача по желанию. Реализовать основной функционал КЧД.
from typing import Any


class Node:
    """
    Класс, представляющий узел в бинарном дереве.
    У каждого узла есть значение (value), а также ссылки на левого (left) и правого (right) потомка.
    Если потомка нет, соответствующее значение равно None
    """

    def __init__(self, value: int):
        """
        Конструктор класса Node
        :param value: целое число
        """
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        """
        Метод форматирует строку, описывающую узел, включая его значение и значения левого и правого потомков,
        если они существуют.
        :return: String
        """
        result = f'значение нашего узла: {self.value}'
        if self.left:
            result += f' значение левого: {self.left.value}'
        if self.right:
            result += f' значение правого: {self.right.value}'
        return result


class BinaryTree:
    """
    Класс, представляющий бинарное дерево.
    """

    def __init__(self, root_value):
        """
        Конструктор класса.
        :param root_value: Значение корневого узла
        """
        self.root = Node(root_value)

    def add(self, *values: int) -> None:
        """
        Метод добавляет новый узел в бинарное дерево.
        :param values: Целое число
        """
        for value in values:
            result = self.search(self.root, value)

            if result[0] is None:
                new_node = Node(value)
                if value > result[1].value:
                    result[1].right = new_node
                else:
                    result[1].left = new_node

    @staticmethod
    def find_min_value_node(node: Node) -> Node:
        """
        Метод позволяет найти узел с минимальным значением в дереве, начиная с заданного узла.
        :param node: Узел, с которого начать поиск
        :return: Узел с минимальным значением
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete_node(self, root_value: Node, value: int) -> Node | None | Any:
        """
        Удаляет узел с заданным значением из дерева, начиная с заданного корневого узла.
        :param root_value: Корневой узел дерева
        :param value: Значение для удаления
        :return: Корневой узел после удаления
        """

        if root_value is None:
            return root_value

        if value < root_value.value:
            root_value.left = self.delete_node(root_value.left, value)
        elif value > root_value.value:
            root_value.right = self.delete_node(root_value.right, value)
        else:
            if root_value.left is None:
                return root_value.right
            elif root_value.right is None:
                return root_value.left

            min_value_node = self.find_min_value_node(root_value.right)
            root_value.value = min_value_node.value
            root_value.right = self.delete_node(root_value.right, min_value_node.value)

        return root_value

    def delete_element(self, *values: int) -> None:
        """
        Метод удаляет элемент с заданным значением из дерева.
        :param values: Целые числа
        :return: None
        """
        for value in values:
            self.root = self.delete_node(self.root, value)

    def search(self, node: Node, value: int, parent=None) -> tuple:
        """
        Метод выполняет рекурсивный поиск узла по значению в бинарном дереве и возвращает узел и его родителя.
        Если узел не найден, он возвращает None и последний просмотренный узел.
        :param node: Узел от которого пойдет поиск
        :param value: Значение искомого узла
        :param parent: Родитель
        :return: Узел и его родитель
        """
        if node is None or value == node.value:
            return node, parent
        if value > node.value:
            return self.search(node.right, value, node)
        if value < node.value:
            return self.search(node.left, value, node)

    def count_elements(self, node: Node = None) -> int:
        """
        Метод подсчитывает количество элементов в бинарном дереве.
        :param node: Узел, от которого начинается подсчет. Если None, то подсчет начинается с корневого узла.
        :return: Количество элементов в дереве.
        """
        if node is None:
            node = self.root
        count = 1
        if node.left is not None:
            count += self.count_elements(node.left)
        if node.right is not None:
            count += self.count_elements(node.right)
        return count

    def show_tree(self, node: Node, level=0) -> None:
        """
        Метод выполняет обход дерева и выводит его на экран.
        :param node: Узел, от которого начинается обход. Если None, то обход начинается с корневого узла.
        :param level: Уровень узла в дереве. Используется для форматирования вывода.
        :return: None
        """
        if node is not None:
            self.show_tree(node.right, level + 1)
            print(f"{' ' * 4 * level} |{'-' * 2}>{node.value}")
            self.show_tree(node.left, level + 1)



bt = BinaryTree(5)
root = bt.root

bt.add(10), bt.add(15), bt.add(3), bt.add(4), bt.add(7), bt.add(1), bt.add(2)
bt.add(11, 14, 21, 34, 8, 6)  # Понты :D
bt.delete_element(4), bt.delete_element(7), bt.delete_element(40)
bt.delete_element(21, 10)

print(f"Количество элементов в древе = {bt.count_elements()}")
bt.show_tree(bt.root)
