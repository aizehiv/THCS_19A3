def tim_so_fibonacci(n):
    if n <= 1:
        return n
    return tim_so_fibonacci(n - 1) + tim_so_fibonacci(n - 2)

print("Bài 10:")
print("Số Fibonacci thứ 10 là:", tim_so_fibonacci(10), "\n")
