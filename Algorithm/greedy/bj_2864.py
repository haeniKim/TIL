# 5와 6의 차이
# 브론즈 2 

a, b = input().split()

sum_min = int(a.replace("6","5")) + int(b.replace("6","5"))

sum_max = int(a.replace("5","6")) + int(b.replace("5","6"))

print(f"{sum_min} {sum_max}")