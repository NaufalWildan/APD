#NIM: 2009106037
nim = int(input("Masukkan nim: "))
n = 1
w = 1
while n <= nim:
    print (w)
    w += 1
    if w == 10:
        w -= 9
    n += 1
