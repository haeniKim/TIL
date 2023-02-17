#세균 증식
def solution(n, t):
    answer = n
    for i in range(t):
        answer *= 2 
    return answer

#더 단순하게
def solution2(n,t):
    return n*(2**t)