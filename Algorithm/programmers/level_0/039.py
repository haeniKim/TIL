#공 던지기
def solution(numbers, k):
    answer = (2 * (k - 1)) % len(numbers) + 1
    return answer