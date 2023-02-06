#특정 문자 제거하기
def solution(my_string, letter):
    answer = ''.join([i for i in my_string if i != letter])
    return answer

#리스트 컴프리헨션으로 letter에 해당하지 않는 값만 담고 join을 통해 하나의 문자열로 만듦
#또 다른 풀이 replace사용 letter를 ''로 바꿈.