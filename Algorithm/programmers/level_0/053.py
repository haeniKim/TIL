#가까운 수
def solution(array, n):
    array.sort()
    cha = [abs(i-n) for i in array]
    return array[cha.index(min(cha))]