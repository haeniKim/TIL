#369게임
def solution(order):
    answer = 0
    for i in str(order):
        if i == '3' or i == '6' or i == '9':
            answer += 1
    return answer

#다른 풀이 count
def solution2(order):
    return sum(map(lambda x: str(order).count(str(x)), [3,6,9]))