#로또 - 당첨 번호 뽑기

from random import randint

def draw_winning_numbers():
    winning_list = []
    i = 0
    while i < 7:
        num = randint(1,45)
        if num not in winning_list:
            winning_list.append(num)
            i += 1
        if i == 6: #당첨번호 6개 정렬
            winning_list.sort()
        
    return winning_list

# lotto_1.py의 함수 사용하기
#def draw_winning_numbers():
#   winning_numbers = generate_numbers(7)
#    return sorted(winning_numbers[:6]) + winning_numbers[6:]
print(draw_winning_numbers())
            