#배열의 유사도
def solution(s1, s2):
    answer = 0
    for i in s1:
        if i in s2:
            answer += 1
    return answer

#다른 풀이 - 수학의 집합 개념 이용. & - 교집합, | = 합집합, - 차집합
def solution2(s1, s2):
    return len(set(s1)&set(s2))