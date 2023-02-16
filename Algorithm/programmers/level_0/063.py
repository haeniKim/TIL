#문자열 계산하기
def solution(my_string):
    exp = my_string.split()
    answer = int(exp[0])
    for i in range(1, len(exp),2):
        if exp[i] == '+':
            answer += int(exp[i+1])
        elif exp[i] == '-':
            answer -= int(exp[i+1])
    return answer

#충격적인 풀이
solution2 = eval