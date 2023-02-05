#짝수 홀수 개수
def solution(num_list):
    odd_num, even_num = 0, 0
    for n in num_list:
        if n % 2 == 0:
            even_num += 1
        else:
            odd_num += 1
    answer = [even_num, odd_num]
    return answer