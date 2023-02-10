#숨어있는 숫자의 덧셈 (1)
def solution(my_string):
    answer = sum([int(i) for i in my_string if i.isdigit()])
    return answer