#최빈값 구하기
def solution(array):
    cnt_dict = {}
    for n in array:
        if n not in cnt_dict.keys():
            cnt_dict[n] = 1
        else:
            cnt_dict[n] += 1
            
    conv_dict = {v:k for k,v in cnt_dict.items()}
    answer = conv_dict.get(max(list(conv_dict.keys())))
    
    if list(cnt_dict.values()).count(max(conv_dict.keys())) > 1:
        answer = -1

    return answer

