#세균 증식
def solution(n, t):
    answer = n
    for i in range(t):
        answer *= 2 
    return answer

#더 단순하게 
def solution2(n,t):
    return n*(2**t)

#시프트 연산 (t만큼 시프트하면 2**t를 곱한 것과 같음)
def solution3(n,t):
    return n << t