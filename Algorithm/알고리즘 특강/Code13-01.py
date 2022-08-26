# 순차 검색
## 함수
import random
def seqSearch(ary, fData) :
    pos = -1
    size = len(ary)
    for i in range(size) :
        if ary[i] == fData:
            pos = i
            break
    return pos



## 변수
dataAry= [random.randint(10,200) for _ in range(20)]
findData = random.choice(dataAry)

## 메인
print('배열 --> ', dataAry)
position = seqSearch(dataAry, findData)
if position == -1 :
    print(f'{findData}는 없음')
else :
    print(f'{findData}는 {position}위치에 있음')