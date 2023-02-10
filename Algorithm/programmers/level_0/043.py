#최댓값 만들기 (1)
def solution(numbers):
    answer = sorted(numbers)[-1] * sorted(numbers)[-2]
    return answer