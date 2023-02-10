#소인수분해
def solution(n):
    answer = []
    for i in range(2, n+1):
        if n % i == 0:
            cnt = 0
            for j in range(1, i+1):
                if i % j == 0:
                    cnt += 1
            if cnt == 2:
                answer.append(i)
    return answer