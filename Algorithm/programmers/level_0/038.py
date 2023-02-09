#2차원으로 만들기     
def solution(num_list, n):
    answer = [[num_list[(i*1) + (j*n)] for i in range(n)] for j in range(int(len(num_list)/n))]
    return answer

#다른 풀이 
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i: i+n])
    return answer