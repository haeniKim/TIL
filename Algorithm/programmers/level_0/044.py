#팩토리얼
def factorial(num):
    if num == 1:
        return 1
    else:
        return factorial(num-1) * num

def solution(n):
    answer = 1
    while True:
        if factorial(answer) > n:
            return answer - 1
        answer += 1

#문제에서 최대의 n 값이 10!보다 작다고 했으므로 간단하게 반복문의 범위를 10까지로 지정할 수 있음
from math import factorial

def solution2(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k