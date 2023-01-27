# 로또 - 번호 뽑기
from random import randint

def generate_numbers(n):
    n_list = []    #리턴할 리스트 생성
    i = 0
    while i < n:
        num = randint(1,45)
        if num not in n_list:
            n_list.append(num)
            i += 1
            
    return n_list
    

print(generate_numbers(6))