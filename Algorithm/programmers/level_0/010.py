#중앙값 구하기

def solution(array):
    array.sort()
    answer = array[len(array)//2]
    return answer