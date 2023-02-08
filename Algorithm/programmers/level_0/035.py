#가위 바위 보
def solution(rsp):
    winning_case = {'2':'0', '0':'5', '5':'2'}
    answer = ''.join([winning_case[i] for i in rsp])
    return answer