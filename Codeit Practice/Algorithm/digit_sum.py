# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    #base case
    if n < 10:
        return n
    
    #recursive case
    return sum_digits(n // 10) + n % 10

# 테스트 코드
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))