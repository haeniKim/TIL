#7의 개수
def solution(array):
    a =''
    for i in array:
        a += str(i)
    answer = a.count('7')
    return answer

#다른 풀이
#리스트 자체를 스트링으로 형 변환해도 가능
def solution2(array):
    return str(array).count('7')