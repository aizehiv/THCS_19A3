s = input("Nhập chuỗi: ")
ket_qua = ""
dang_trang = False

for ch in s:
    if ch == " ":
        if not dang_trang:
            ket_qua += ch
        dang_trang = True
    else:
        ket_qua += ch
        dang_trang = False

print(ket_qua)
