def tinh_tong_chu_so(n):
    if n < 10:
        return n
    return n % 10 + tinh_tong_chu_so(n // 10)

print("Bài 9:")
print("Tổng chữ số của 1234 là:", tinh_tong_chu_so(1234), "\n")
