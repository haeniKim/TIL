#자릿수 더하기
def solution(n):
    answer = sum([int(i) for i in str(n)])
    return answer