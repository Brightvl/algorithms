import random
import time


def how_long(func, x):
    start = time.time()
    func(x)
    print(f"На это ушло времени {time.time() - start}")


# Задание 1
# 1.Необходимо написать один из простых алгоритмов сортировки, имеющий сложность O(n2).
# 2.Можно выбрать из пузырьковой сортировки, сортировки вставками и
# сортировки выбором.
# 3.Следует обратить внимание на сложность данных алгоритмов и
# указать признаки квадратичной сложности для каждого из них

def sorting(array: list):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


# Задание 2
# Написать алгоритм быстрого поиска (quicksort).
def quick_sort(array: list):
    if len(array) <= 1:
        return array
    q = random.choice(array)
    left_array = []
    middle_array = []
    right_array = []
    for el in array:
        if el == q:
            middle_array.append(el)
        elif el < q:
            left_array.append(el)
        else:
            right_array.append(el)
    return quick_sort(left_array) + middle_array + quick_sort(right_array)

    # Сортировка целых чисел
    # Исходная последовательность чисел длины n, а в конце отсортированная, хранится в массиве A.
    # Также используется вспомогательный массив C с индексами от 0  до k−1, изначально заполняемый нулями.
    # Последовательно пройдём по массиву A и запишем в C[i] количество чисел, равных i.
    # Теперь достаточно пройти по массиву C и для каждого number∈{0,...,k−1}  в массив A
    # последовательно записать число C[number] раз.


def counting_sort(array: list):
    temp_array = [0] * (max(array) + 1)
    for el in array:
        temp_array[el] += 1
    result_array = []
    for i in range(len(temp_array)):
        result_array += [i] * temp_array[i]
    return result_array


def merge_two_list(a, b):
    """
    Сортировка слиянием
    :param a:
    :param b:
    :return:
    """
    result = []
    while a and b:
        result.append((a if a[0] < b[0] else b).pop(0))
    result += a + b
    return result


def merge_sort(s):
    mid = len(s) // 2
    return s if len(s) == 1 else merge_two_list(merge_sort(s[:mid]), merge_sort(s[mid:]))


def heap_sort(array: list):
    """
    Эта функция выполняет сортировку кучей.
    Вызывает build_heap() для построения начальной кучи.
    Затем она итерируется по массиву, начиная с последнего элемента и перемещая
    наибольший элемент (корень кучи) в конец массива.
    После этого уменьшается размер кучи, и куча пересортировывается, чтобы выбрать следующий наибольший элемент.
    """
    build_heap(array)
    array_size = len(array)
    for i in range(array_size - 1, 0, -1):
        array[0], array[i] = array[i], array[0],
        reduce_heap_size(array, i, 0)


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
    :param array: Целочисленный массив
    :param array_size:
    :param root:
    """
    max = root
    left = 2 * root + 1
    right = 2 * root + 2
    # Сравниваем корень с левым потомком, если такой существует
    if left < array_size and array[left] > array[max]:
        max = left
    # Сравниваем корень с правым потомком, если такой существует
    if right < array_size and array[right] > array[max]:
        max = right
    # Если максимальный элемент не является текущим корнем, меняем их местами
    if max != root:
        array[root], array[max] = array[max], array[root]
        # Рекурсивно вызываем функцию для пересортировки поддерева
        reduce_heap_size(array, array_size, max)


new_list = [random.randint(0, 1_000_000) for _ in range(10_000)]
# print(new_list)

# HW
print("heap_sort")
list_heap = new_list[::]
# print(list_heap)
start = time.time()
heap_sort(list_heap)
# print(list_heap)
print(f"На это ушло времени {time.time() - start}")

print("Merger sort")
list_1 = new_list[::]
start = time.time()
merge_sort(list_1)
print(f"На это ушло времени {time.time() - start}")

print("Counting sort")
how_long(counting_sort, new_list)

print("Built in sorting")
list_2 = new_list[::]
start = time.time()
list_2.sort()
print(f"На это ушло времени {time.time() - start}")

print("Quick sort")
start = time.time()
quick_sort(new_list)
print(f"На это ушло времени {time.time() - start}")

print("Bubble sort")
how_long(sorting, new_list)
# print(new_list)


# print(counting_sort([1, 4, 7, 9, 4, 2, 7, 15, 5, 3, 3, 6, 3, 5]))
