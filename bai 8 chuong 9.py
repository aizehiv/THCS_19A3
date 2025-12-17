def tim_so_le_lon_nhat(a, b, c):
    so_le = [x for x in (a, b, c) if x % 2 == 1]
    return max(so_le) if so_le else -1

print("Bài 8:")
print("Số lẻ lớn nhất trong (4,7,9) là:", tim_so_le_lon_nhat(4, 7, 9), "\n")
