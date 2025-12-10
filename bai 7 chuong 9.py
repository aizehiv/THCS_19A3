def tinh_tong_so_hoan_hao(a, b):
    tong = 0
    for num in range(a, b + 1):
        tong_uoc = 0
        for i in range(1, num):
            if num % i == 0:
                tong_uoc += i
        if tong_uoc == num:
            tong += num
    return tong

print("Bài 7:")
print("Tổng số hoàn hảo từ 1 đến 10000:", tinh_tong_so_hoan_hao(1, 10000), "\n")
