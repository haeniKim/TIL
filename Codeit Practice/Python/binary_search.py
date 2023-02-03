#이진탐색 알고리즘

def binary_search(element, some_list):
    f_index = 0
    l_index = len(some_list) -1
    while f_index <= l_index:
        mid_index = (f_index + l_index) // 2
        if element == some_list[mid_index]:
            return mid_index
        elif element > some_list[mid_index]:
            f_index = mid_index + 1
        elif element < some_list[mid_index]:
            l_index = mid_index - 1
    return None