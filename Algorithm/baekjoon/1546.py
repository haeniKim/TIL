n = int(input())
scores = list(map(int, input().split()))
new_scores = [scores[i]/max(scores)*100 for i in range(n)]
print(sum(new_scores)/n)