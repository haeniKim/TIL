#인덱스 바꾸기
def solution(my_string, num1, num2):
    list_ms = list(my_string)
    list_ms[num1],list_ms[num2] = list_ms[num2],list_ms[num1]
    answer = ''.join(list_ms)
    return answer