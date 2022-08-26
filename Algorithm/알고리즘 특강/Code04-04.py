#단순 연결 리스트 실무ver.

## 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start): #출력을 위한 함수
    current = start
    print(current.data, end = ' ')
    while (current.link != None):
        current = current.link
        print(current.data, end= ' ')
    print()

def insertNode(findData, insertData) :
    global memory, head, pre, current
    #case1 : 헤드 앞에 삽입
    if head.data == findData :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    #case2 : 중간 노드 앞에 삽입. 사나 앞에 솔라
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == findData :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    #case3 : 마지막에 삽입. (없는)재남 뒤에 문별
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    return

def deleteNode(deleteData) :
    global memory, head, pre, current
    # 케이스1 : 삭제할게 머리인 경우. '다현'
    if head.data == deleteData :
        current = head
        head = head.link
        del(current)
        return
    # 케이스2 : 중간 노드 삭제할 경우. '쯔위'
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == deleteData :
            pre.link = current.link
            del(current)
            return
    # 케이스3 : 없는걸 지울때. '재남'
    return

    
def findNode(findData) :
    global memory, head, pre, current
    current = head
    if current.data == findData :
        return current
    while current.link != None :
        current = current.link
        if current.data == findData :
            return current
    return Node() #원하는 게 없으면 빈 도드 출력하도록


## 변수
memory = [] #넣을 메모리
head, pre, current = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효'] #실제로 처리할 데이터 넣을 곳, 실시간 / 응용-리스트 부분 수정

## 메인
node = Node() #무조건 첫번째 노드는 따로 만들기, / 임시노드 개념으로 재사용
node.data = dataArray[0]
head = node #중요한 개념
memory.append(node)

for data in dataArray[1:]:
    pre = node #중요한 개념
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)



#insertNode('다현', '화사') # case1. head 앞에 삽입하는 경우
#printNodes(head)

#insertNode('사나', '솔라')
#printNodes(head)

#insertNode('해니', '문별')
#printNodes(head)

#deleteNode('다현') #head 삭제
#printNodes(head)

#deleteNode('쯔위') 
#printNodes(head)

fNode = findNode('사나') #찾아서 돌려받기 /덩어리
print(fNode.data)
