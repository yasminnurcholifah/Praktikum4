print("Nama : Siti Yasmin Nurcholifah")
print("NIM : 312210057")

print("Membuat List Sebanyak 5 Elemen dengan Nilai Bebas")
a = []
a = [20, 30, 50, 70, 100]
print(a)
print(a[2])
print(a[1:3])
print(a[4])

print("-----------------------------------------------------------------------")

a[3] = 90
print(a[3])
a[3:4] = 90, 80
print(a[3:4])

print("-----------------------------------------------------------------------")

b = a[0:2]
print(b)
b.append(35)
print(b)
b.extend([2,6,10])
print(b)
c = a+b
print(c)