#영어가 싫어요
def solution(numbers):
    num = ['zero','one','two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine']
    for i in range(10):
        numbers = numbers.replace(num[i], str(i))
    answer = int(numbers)
    return answer