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
