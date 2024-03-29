# 1이 될 때까지
# 어떠한 수 N이 1이 될 때까지 두 과정 중 하나를 반복적으로 선택하여 수행
# 단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.

# N과 K가 주어질 때 N이 1이 될 때까지 1번, 혹은 2번의 과정을 수행해야 하는 최소 횟수 구하기

def until_1(n, k):
    cnt = 0
    while True:
        if n % k == 0:
            n //= k
            cnt += 1
        else:
            n -= 1
            cnt += 1
        if n == 1:
            break
    return cnt

n, k = map(int, input().split())
print(until_1(n, k))


## --- 다른 풀이 ---
n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target 

    # N이 K보다 작을 때 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)