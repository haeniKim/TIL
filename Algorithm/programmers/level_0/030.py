#외계행성의 나이
def solution(age):
    al_age = ['a','b','c','d','e','f','g','h','i','j']
    answer = ''.join([al_age[int(i)] for i in str(age)] )
    return answer