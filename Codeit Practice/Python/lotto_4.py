#로또 - 당첨금 확인
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
    return prize_money

# 테스트 코드
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))