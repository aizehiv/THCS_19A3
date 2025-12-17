def kiem_tra_so_armstrong(n):
    tong = sum(int(ch)**3 for ch in str(n))
    return tong == n

print("Bài 3:")
print("153 có phải Armstrong?", kiem_tra_so_armstrong(153), "\n")

