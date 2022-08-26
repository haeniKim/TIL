#완전한 이진 탐색 트리(*)

## 함수
class TreeNode() :
    def __init__(self) :
        self.left = None
        self.data = None
        self.right = None


## 변수
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳','마마무','에이핑크','걸스데이','트와이스'] #바꿀 데이터 부분


## 메인
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:] :
    node = TreeNode()
    node.data = name

    current = root #현재 위치 무조건 루트부터 시작
    while True :
        if name < current.data :
            if current.left == None :
                current.left = node
                break
            current = current.left
        else :
            if current.right == None :
                current.right = node
                break
            current = current.right

    memory.append(node)

print("이진 탐색 트리 구성 완료!")

findName = '마마무'
current = root
while True :
    if findName == current.data :
        print(findName, '을 찾았음')
        break
    elif findName < current.data :
        if current.left == None :
            print(findName, ' 트리에 없습니다')
            break
        current = current.left
    else :
        if current.right == None :
            print(findName, ' 트리에 없습니다')
            break
        current = current.right