def kiem_tra_so_doi_xung(n):
    return str(n) == str(n)[::-1]

print("Bài 5:")
print("121 có phải đối xứng?", kiem_tra_so_doi_xung(121), "\n")
