#컨트롤 제트
def solution(s):
    n_list = s.split()
    for i in range(len(n_list)):
        if n_list[i] == 'Z':
            n_list[i-1], n_list[i] = '0', '0'
    answer = sum([int(i) for i in n_list])
    return answer

#더 나은 풀이
def solution2(s):
    answer = 0
    n_list = s.split()
    for i in range(len(n_list)):
        answer += int(n_list[i]) if n_list[i] != 'Z' else -int(n_list[i-1])
    return answer