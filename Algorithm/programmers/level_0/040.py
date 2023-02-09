#배열 회전시키기
def solution(numbers, direction):
    if direction == "right":
        answer = [numbers[-1]] + numbers[0:-1]
    elif direction == "left":
        answer = numbers[1:] + [numbers[0]]
    return answer