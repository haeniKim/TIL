# 잃어버린 괄호
# 실버 2

# 문제: 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.
# 출력 : 첫째 줄에 정답을 출력한다.

expr = input()

if '-' in expr:
    result, expr_list = sum([int(i) for i in expr.split('-')[0].split('+')]), expr.split('-')[1:]

    for e in expr_list:
        #result -= eval(e)
        if '+' in e:
            result -= sum([int(i) for i in e.split('+')])
        else:
            result -= int(e)
else:
    result = sum([int(i) for i in expr.split('+')])

print(result)

# --- 다른 풀이 ---
expr = input().split('-')

result = 0
for e in expr[0].split('+'):
    result += int(e)

for i in expr[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)