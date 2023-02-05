#문자 반복 출력하기
def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += (i * n)
    return answer


#def solution(my_string, n):
#    return ''.join(i*n for i in my_string)