#가장 큰 수 찾기
def solution(array):
    answer = [max(array), array.index(max(array))]
    return answer