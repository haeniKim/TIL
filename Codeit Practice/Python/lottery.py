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

def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for i in winning_numbers:
        if i in numbers:
            count += 1
    return count

def check(numbers, winning_numbers):
    matching_cnt = count_matching_numbers(numbers, winning_numbers[:-1]) #보너스 번호를 제외하고 번호 비교
    
    if matching_cnt == 6:
        prize_money = 1000000000
    elif matching_cnt == 5 and winning_numbers[6] in numbers: #5개 + 보너스 번호 일치
        prize_money = 50000000
    elif matching_cnt == 5:
        prize_money = 1000000 
    elif matching_cnt == 4:
        prize_money = 50000 
    elif matching_cnt == 3:
        prize_money = 5000
    else:
        prize_money = 0 
    return prize_money