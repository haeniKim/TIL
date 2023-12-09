# 3-1 거스름돈

# 동전 500, 100, 50, 10
# 손님에게 거슬러 줄 돈 N원일 때, 거슬러 줘야 할 동전 최소 개수., N은 10의 배수

n = 1260
cnt = 0


coin_type = [500, 100, 50, 10]

for coin in coin_type:
    cnt += n // coin
    n %= coin

print(cnt)

