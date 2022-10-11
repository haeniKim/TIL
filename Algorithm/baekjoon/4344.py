n = int(input())
for i in range(n):
    cnt = 0
    scores = list(map(int, input().split()))
    for j in scores[1:]:
        if j > sum(scores[1:]) / scores[0]:
            cnt += 1
    mean_p = cnt / scores[0] * 100
    print("{:0.3f}%".format(mean_p))