#구슬을 나누는 경우의 수
def solution(balls, share):
    numer, denom = 1, 1
    for i in range(share):
        numer *= balls - i
        denom *= i + 1 
    answer = int(numer / denom)
    return answer