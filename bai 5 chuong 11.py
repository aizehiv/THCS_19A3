a = list(map(int, input().split()))
b = []

for x in a:
    da_co = False
    for y in b:
        if x == y:
            da_co = True
            break
    if not da_co:
        b.append(x)

print(b)
