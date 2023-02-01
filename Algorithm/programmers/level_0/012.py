#짝수는 싫어요 #리스트 컴프리헨션 사용

def solution(n):
    answer = [i for i in range(1, n+1) if i % 2 == 1]
    return answer

#다른 풀이 - 조건문 없이

#def solution(n):
#    return [i for i in range(1, n+1, 2)]
