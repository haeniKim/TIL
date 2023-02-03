#선형 탐색 알고리즘

def linear_search(element, some_list):
    for i in some_list:
        if i == element:
            return some_list.index(i)
    return None