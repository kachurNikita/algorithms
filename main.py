from collections import defaultdict
from collections import deque

selection_sort_arr = [8, 11, -1, 24, 0, 3, 2, -100]

def selection_sort(array):
    for i in range(len(array)):
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


selection_sort(selection_sort_arr)

# Bubble sort algorithm / sorting algorithm O(N**2) time complexity
bubble_sort_arr = [1, -1, 5, 2, 9, 4]


def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - 1):
            if array[j + 1] < array[j]:
                array[j + 1], array[j] = array[j], array[j + 1]
    return array

# print(bubble_sort(bubble_sort_arr))


# Quick sort algorithm / sorting algorithm O(n**2) time complexity

quick_sort_array = [4, 1, 3, 7, 5, 0, 9, 2]


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


def pre_merge_sort(arr_1, arr_2):
    new_list = []
    i = j = 0
    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] < arr_2[j]:
            new_list.append(arr_1[i])
            i += 1
        else:
            new_list.append(arr_2[j])
            j += 1
    while i < len(arr_1):
        new_list.append(arr_1[i])
        i += 1
    while j < len(arr_2):
        new_list.append(array_2[j])
        j += 1
    return new_list


# print(pre_merge_sort(array_1, array_2))

merge_sort_arr = [3, 4, 2, 1, -10, 11, 22, 35, 0]


def divide_and_conquer(arr):
    if len(arr) == 1:
        return arr
    else:
        middle = len(arr) // 2
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


# print(divide_and_conquer(merge_sort_arr))


# Breadth First Search


class TreeNode:
    def __init__(self, left_node, right_node, value):
        self.left_node = left_node
        self.right_node = right_node
        self.value = value


left_child_child = TreeNode(None, None, 5)

right_child_child = TreeNode(None, None, 100)

left_child = TreeNode(left_child_child, None, 11)

right_child = TreeNode(None, right_child_child, 1)

tree_node = TreeNode(left_child, right_child, 10)


def bfs(tree, target):
    if tree:
        print(tree.value)
        if tree.value == target:
            return tree.value
        else:
            left_part = bfs(tree.left_node, target)
            if left_part:
                return left_part
            right_part = bfs(tree.right_node, target)
            return right_part


# print(bfs(tree_node, 100))
#


# Depth First Search
#
# Using a Python dictionary to act as an adjacency list

# graph = {
#   '5': ['3', '7'],
#   '3': ['2', '4'],
#   '7': ['8'],
#   '2': [],
#   '4': ['8'],
#   '8': []
# }
#
# visited = set() # Set to keep track of visited nodes of graph.
#
#
# def dfs(graph, node, visited):
#     if node not in visited:
#         visited.add(node)
#         for neibhour in graph[node]:
#             dfs(graph, neibhour, visited)
#
#
# dfs(graph, '5', visited)


# graph = {
#     'you': ['Alice', 'Bob', 'Claire'],
#     'Alice': ['Peggy'],
#     'Claire': ['Jonny', 'Thom'],
#     'Bob': ['Anuj', 'Peggy'],
#     'Anuj': [],
#     'Peggy': [],
#     'Thom': [],
#     'Jonny': [],
# }

# initialize our queue structure
# search_queue = deque()
# search_queue += graph['you']
#
#
# def find_mango_seller(structure):
#     while structure:
#         person = structure.popleft()
#         if person_is_seller(person):
#             print(f'The person {person} is seller!')
#             return True
#         else:
#             structure += graph[person]
#     return False
#
#
# def person_is_seller(name):
#     if name == 'Jonny':
#         return name
#
#
# find_mango_seller(search_queue)

my_structure = {

    '8': ['3', '1', '6', '7', '5'],
    '5': [],
    '1': [],
    '3': [],
    '6': ['9'],
    '7': ['4'],
    '4': [],
    '9': ['2'],
    '2': []
}

my_graph = {
    '9': ['6', '1'],
    '6': ['8', '21'],
    '1': ['4', '3'],
    '8': [],
    '21': [],
    '4': [],
    '3': [],
}

#
# def bfs_practice(graph, vertex):
#     counter = 0
#     # this structure (queue) will help me to check adjacent vertexes.
#     queue = deque()
#     # I need to know which vertex was visited!
#     visited = []
#     # So  i added vertex to visited
#     visited.append(vertex)
#     # and add vertex to be checked in FIFO order
#     # (first vertex was found, added, second, added, and them first will out first too
#     queue.append(vertex)
#     while queue:
#         counter += 1
#         vertex = queue.popleft()
#         # print(vertex)
#         for i in graph[vertex]:
#             if i not in visited:
#                 visited.append(i)
#                 queue.append(i)
#     return counter
#
# print(bfs_practice(my_structure, '6'))
#
#



# def traversal_tree(tree):
#     queue = []
#     queue.append(tree)
#     values = []
#     while len(queue) != 0:
#         current_vertex = queue.pop(0)
#         values.append(current_vertex.val)
#         if current_vertex.left:
#             queue.append(current_vertex.left)
#         if current_vertex.right:
#             queue.append(current_vertex.right)
#     print(values)
#
#
# traversal_tree(main_tree)

# print(traversal_tree(main_tree))
# class Node:
#   def __init__(self, value, left=None, right=None):
#     self.value = value
#     self.left = left
#     self.right = right
#
#
# tree = Node(47)  # The root node of our binary tree
# tree.left = Node(36)
# tree.right = Node(66)
#
# tree.left.left = Node(25)
# tree.left.right = Node(39)
# tree.left.right.left = Node(38)
# tree.left.right.right = Node(42)
#
# tree.right.left = Node(63)
# tree.right.left.right = Node(64)
# tree.right.right = Node(68)
#

# def taversal_tree(tree):
#     queue = [tree]
#     visited = []
#     while len(queue) != 0:
#         current_vertex = queue.pop(0)
#         visited.append(current_vertex.value)
#         if current_vertex.left:
#             queue.append(current_vertex.left)
#         if current_vertex.right:
#             queue.append(current_vertex.right)
#     print(visited)
#     value = int(input('Enter value what you are look for: '))
#     node = tree
#     found = False
#     while node and value:
#         if value == node.value:
#             found = True
#             print('Value found')
#             break
#         elif value <= node.value:
#             node = node.left
#         elif value > node.value:
#             node = node.right
#     if not found:
#         print('Not found')
#
#
# print(taversal_tree(tree))



class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def __repr__(self):
        return f'{self.value}'


parent_node = Node(4)
parent_node.right = Node(6)
parent_node.right.right = Node(7)
parent_node.right.right.right = Node(9)
parent_node.right.right.right.right = Node(8)
parent_node.right.right.right.right.left = Node(5)
parent_node.right.right.right.right.right = Node(1)
parent_node.right.right.right.right.right.left = Node(14)
parent_node.right.right.right.right.right.right = Node(6)
parent_node.right.right.right.right.right.right.left = Node(3)
parent_node.right.right.right.right.right.right.right = Node(2)


def breadth_first_search(tree, target):
    queue = [tree]
    visited_nodes = []
    while len(queue) != 0:
        current_node = queue.pop(0)
        if current_node.value == target:
            return 'Value found'
        visited_nodes.append(current_node.value)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    else:
        return 'Value not found'


print(breadth_first_search(parent_node, 2))

