
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


# selection_sort(arr)

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


# print(quick_sort(quick_sort_array))


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


# print(binary_search(binary_search_arr, 1))


# I didn't find algorithm name, but anyway it is  necessary to understand, in order to learn merge_sort
array_1 = [2, 4, 5, 8, 21, 50]
array_2 = [-10, 0, 6, 11, 18]

# -10, 0, 2, 4, 5, 6, 8, 11, 18,


# def pre_merge_sort(arr_1, arr_2):
#     new_list = []
#     i = j = 0
#     while i < len(arr_1) and j < len(arr_2):
#         if arr_1[i] < arr_2[j]:
#             new_list.append(arr_1[i])
#             i += 1
#         else:
#             new_list.append(arr_2[j])
#             j += 1
#     while i < len(arr_1):
#         new_list.append(arr_1[i])
#         i += 1
#     while j < len(arr_2):
#         new_list.append(array_2[j])
#         j += 1
#     return new_list


# print(pre_merge_sort(array_1, array_2))

merge_sort_arr = [3, 4, 2, 1, -10, 11, 22, 35, 0]


def divide_and_conquer(arr):
    if len(arr) == 1:
        return arr
    else:
        middle = len(arr)// 2
        left_part = divide_and_conquer(arr[:middle])
        right_part = divide_and_conquer(arr[middle:])
        return merge_sort(left_part, right_part)


def merge_sort(arr_1, arr_2):
    sorted_arr = []
    i = j = 0
    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] < arr_2[j]:
            sorted_arr.append(arr_1[i])
            i += 1
        else:
            sorted_arr.append(arr_2[j])
            j += 1
    if i < len(arr_1):
        sorted_arr += arr_1[i:]
    else:
        sorted_arr += arr_2[j:]
    return sorted_arr


print(divide_and_conquer(merge_sort_arr))


















