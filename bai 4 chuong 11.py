a = list(map(int, input().split()))

max1 = None
max2 = None

for x in a:
    if max1 is None or x > max1:
        max2 = max1
        max1 = x
    elif x != max1 and (max2 is None or x > max2):
        max2 = x

print("Lớn thứ hai:", max2)
