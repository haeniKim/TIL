#피자 나눠 먹기(2)

import math

def solution(n):
    answer = (n * 6) // math.gcd(n, 6) // 6
    return answer