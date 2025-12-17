A = set(map(int, input().split()))
B = set(map(int, input().split()))

giao = set()
hieuA = set()
hieuB = set()

for x in A:
    if x in B:
        giao.add(x)
    else:
        hieuA.add(x)

for x in B:
    if x not in A:
        hieuB.add(x)

print(giao, hieuA, hieuB)
