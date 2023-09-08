import time
import random


def heap_sort(array: list):
    """
    Эта функция выполняет сортировку кучей.
    Вызывает build_heap() для построения начальной кучи.
    Затем она итерируется по массиву, начиная с последнего элемента и перемещая
    наибольший элемент (корень кучи) в конец массива.
    После этого уменьшается размер кучи, и куча пересортировывается, чтобы выбрать следующий наибольший элемент.
    """
    array_copy = array[::]
    build_heap(array_copy)
    array_size = len(array_copy)
    for last_idx in range(array_size - 1, 0, -1):
        array_copy[0], array_copy[last_idx] = array_copy[last_idx], array_copy[0],
        reduce_heap_size(array_copy, last_idx, 0)
    return array_copy


def build_heap(array: list):
    """
    Функция строит начальную кучу из массива.
    Начинается с середины массива и поочередно пересортировывает элементы вниз по дереву.
    """
    array_size = len(array)
    # Начинаем с середины массива и идем к началу
    for root in range(array_size // 2 - 1, -1, -1):
        reduce_heap_size(array, array_size, root)


def reduce_heap_size(array: list, array_size, root):
    """
    Эта функция рекурсивно пересортирует поддерево с корнем в позиции i, чтобы удовлетворить условия кучи.
    Она сравнивает корень с его потомками и, если необходимо, меняет элементы местами,
    а затем рекурсивно вызывает себя для дальнейшей пересортировки.
    """
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2
    # Сравниваем корень с левым потомком, если такой существует
    if left < array_size and array[left] > array[largest]:
        largest = left
    if right < array_size and array[right] > array[largest]:
        largest = right
    # Если максимальный элемент не является текущим корнем, меняем их местами
    if largest != root:
        array[root], array[largest] = array[largest], array[root]
        # Рекурсивно вызываем функцию для пересортировки поддерева
        reduce_heap_size(array, array_size, largest)


print("heap_sort")
new_list = [random.randint(0, 10) for _ in range(6)]
start_time = time.time()
sorted_array = heap_sort(new_list)
print(f"Elapsed time {time.time() - start_time}")
