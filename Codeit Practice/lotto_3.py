#로또 - 겹치는 번호 개수
def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for i in winning_numbers:
        if i in numbers:
            count += 1
    return count


# 테스트 코드
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))