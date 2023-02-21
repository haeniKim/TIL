#숨어있는 숫자의 덧셈 (2)
def solution(my_string):
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i,' ')
    num_list = map(int, my_string.split())
    return sum(num_list)

#다른 사람의 풀이 - 더 깔끔하게 
def solution2(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())