
# Selection sort algorithm / sorting algorithm, O(N**2) time complexity

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
            array[i], array[index] = array[index], array[i]
    return array

selection_sort(arr)

# Bubble sort algorithm / sorting algorithm O(N**2) time complexity
bubble_arr = [1, -1, 5, 2, 9, 4]

def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - 1):
            if array[j + 1] < array[j]:
                array[j + 1], array[j] = array[j], array[j + 1]
    return array

# print(bubble_sort(bubble_arr))


# Quick sort algorithm / sorting algorithm O(n**2) time complexity

quick_sort_array = [4, 1, 3, 7, 5, 0, 9, 2,]

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        left_arr = []
        right_arr = []
        pivot = array[0]
        for l in range(len(array)):
            if array[l] < pivot:
                left_arr.append(array[l])
        for b in range(len(array)):
            if array[b] > pivot:
                right_arr.append(array[b])
        return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)


print(quick_sort(quick_sort_array))


# Binary search algorithm / searching algorithm O(log N) time complexity
binary_search_arr = [1, 20, 22, 25, 30, 50]


def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return True
        elif array[middle] < target:
            left = middle + 1
        elif array[middle] > target:
            right = middle - 1
    return False


print(binary_search(binary_search_arr, 1))