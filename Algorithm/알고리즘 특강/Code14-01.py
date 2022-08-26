#재귀
## 함수
def openBox() :
    global count
    print('상자를 엽니다:)')
    count -= 1
    if count == 0 :
        print('** 선물 **')
        return # 이전에 호출한 곳
    openBox()
    print('상자를 닫습니다.')

## 변수
count = 10


## 메인
openBox()