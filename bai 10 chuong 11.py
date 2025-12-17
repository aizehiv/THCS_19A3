n = int(input())
m = int(input())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

max_tong = None
hang = 0

for i in range(n):
    tong = 0
    for j in range(m):
        tong += a[i][j]
    if max_tong is None or tong > max_tong:
        max_tong = tong
        hang = i

print("Hàng:", hang)
