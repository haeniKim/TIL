#암호 해독
def solution(cipher, code):
    answer = ''
    for n,i in enumerate(cipher):
        if (n+1) % code == 0:
            answer += i
    return answer

#다른 풀이
def solution2(cipher, code):
    answer = cipher[code-1::code]
    return answer