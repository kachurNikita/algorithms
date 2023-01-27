arr = [8, 11, -1, 24, 0, 3, 2, -100]


def selection_sort(array):
    for i in range(len(array) - 1):
        min_value = array[i]
        index = i
        for j in range(i + 1, len(array)):
            if min_value > array[j]:
                min_value = array[j]
                index = j

        if index != i:
            # old_value
            temporary_var = array[i]
            array[i] = array[index]
            array[index] = temporary_var
    return array




bubble_arr = [1, -1, 5, 2, 9, 4]

def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - 1):
            if array[j + 1] < array[j]:
                array[j + 1], array[j] = array[j], array[j + 1]
    return array




print(bubble_sort(bubble_arr))