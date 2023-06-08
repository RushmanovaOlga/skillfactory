def my_sort(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1

        array[idx] = x
    return array


def binary_search(array, element, left, right):
    if element > max(array) or element < min(array):
        return False

    if array[right] < element:
        return right

    if array[left] >= element:
        return left - 1

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:

        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


unsorted_array = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
element = int(input("Введите любое число: "))
sorted_array = my_sort(unsorted_array)
print("Отсортированный список по возрастанию элементов ", sorted_array)
index = binary_search(sorted_array, element, 0, len(sorted_array) - 1)
print("Номер позиции элемента", index)
