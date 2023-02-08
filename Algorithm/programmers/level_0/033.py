#개미 군단
def solution(hp):
    answer = (hp // 5) + (hp % 5) // 3 + (hp % 5) % 3
    #장군개미 (hp // 5)
    #병정개미 (hp % 5) // 3
    #일개미 (hp % 5) % 3
    return answer