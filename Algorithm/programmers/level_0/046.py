#문자열 정렬하기 (1)
def solution(my_string):        
    answer = sorted([int(i) for i in my_string if i.isnumeric()])
    return answer