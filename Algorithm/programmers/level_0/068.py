#OX퀴즈
def solution(quiz):
    answer = []
    for exp in quiz:
        qst = exp.split()
        if qst[1] == '+':
            result = int(qst[0]) + int(qst[2])
        else:
            result = int(qst[0]) - int(qst[2])
        if result == int(qst[4]):
            answer.append("O")
        else:
            answer.append("X")
    return answer